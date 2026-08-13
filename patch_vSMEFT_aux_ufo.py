#!/usr/bin/env python3
"""Install exact non-propagating auxiliary propagators in a FeynRules UFO.

Usage:
    python3 patch_vSMEFT_aux_ufo.py /absolute/path/to/generated_UFO

Run this after exporting ``Leff4fermions1Aux`` from
``vSMEFT_4-fermions_single-N_aux.fr`` or ``Leff4fermions2Aux`` from
``vSMEFT_4-fermions_pair-N_aux.fr``. The operation is idempotent and creates
``*.pre_aux_patch`` backups before the first modification.
"""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


PROPAGATOR_MARKER = "# BEGIN VSMEFT NONPROPAGATING AUXILIARIES"
PROPAGATOR_BLOCK = r'''

# BEGIN VSMEFT NONPROPAGATING AUXILIARIES
# The explicit factors of i follow the convention of the FeynRules-generated
# propagators shipped with this model. Mass(id) is set to Lambda for every
# auxiliary particle by this patch; it is a normalization, not a pole mass.
AuxScalarPlus = Propagator(
    name = "AuxScalarPlus",
    numerator = "complex(0,1)",
    denominator = "Mass(id)**2"
)

AuxScalarMinus = Propagator(
    name = "AuxScalarMinus",
    numerator = "complex(0,-1)",
    denominator = "Mass(id)**2"
)

AuxVectorPlus = Propagator(
    name = "AuxVectorPlus",
    numerator = "complex(0,1) * Metric(1,2)",
    denominator = "Mass(id)**2"
)

AuxVectorMinus = Propagator(
    name = "AuxVectorMinus",
    numerator = "complex(0,-1) * Metric(1,2)",
    denominator = "Mass(id)**2"
)
# END VSMEFT NONPROPAGATING AUXILIARIES
'''


def backup(path: Path) -> None:
    target = path.with_name(path.name + ".pre_aux_patch")
    if not target.exists():
        shutil.copy2(path, target)


def particle_blocks(text: str):
    """Yield (start, end, block) for top-level Particle(...) expressions."""
    for match in list(re.finditer(r"\bParticle\(", text)):
        start = match.start()
        pos = match.end()
        depth = 1
        quote = None
        escaped = False
        while pos < len(text) and depth:
            char = text[pos]
            if quote:
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == quote:
                    quote = None
            else:
                if char in "'\"":
                    quote = char
                elif char == "(":
                    depth += 1
                elif char == ")":
                    depth -= 1
            pos += 1
        if depth == 0:
            yield start, pos, text[start:pos]


def auxiliary_propagator(name: str) -> str:
    is_vector = name.startswith(("x_dune_", "x_pair_"))
    # U and V are deliberately opposite-sign propagators.
    is_minus = bool(re.search(r"_(?:v0|vm|vp|vu|vd)(?:_|~|$)", name))
    kind = "Vector" if is_vector else "Scalar"
    sign = "Minus" if is_minus else "Plus"
    return f"Prop.Aux{kind}{sign}"


def patch_particle_block(block: str) -> tuple[str, bool]:
    name_match = re.search(r"\bname\s*=\s*['\"]([^'\"]+)['\"]", block)
    if not name_match or not name_match.group(1).startswith("x_"):
        return block, False

    name = name_match.group(1)
    prop = auxiliary_propagator(name)

    block, n_mass = re.subn(r"\bmass\s*=\s*[^,\n]+", "mass = Param.Lambda", block, count=1)
    if n_mass != 1:
        raise RuntimeError(f"Could not replace the mass of auxiliary particle {name}")

    if re.search(r"\bpropagating\s*=", block):
        block = re.sub(r"\bpropagating\s*=\s*(?:True|False)", "propagating = False", block, count=1)
    else:
        block = re.sub(
            r"\)(\s*)$",
            lambda match: ",\n             propagating = False" + match.group(1) + ")",
            block,
            count=1,
        )

    if re.search(r"\bpropagator\s*=", block):
        block = re.sub(r"\bpropagator\s*=\s*[^,\n)]+", f"propagator = {prop}", block, count=1)
    else:
        block = re.sub(
            r"\)(\s*)$",
            lambda match: f",\n             propagator = {prop}" + match.group(1) + ")",
            block,
            count=1,
        )

    # The two insertions above can leave a comma immediately after the final
    # existing argument, which is valid, but never allow a doubled comma.
    block = block.replace(",,", ",")
    return block, True


def patch_particles(path: Path) -> int:
    text = path.read_text()
    replacements = []
    count = 0
    for start, end, block in particle_blocks(text):
        new_block, changed = patch_particle_block(block)
        if changed:
            replacements.append((start, end, new_block))
            count += 1
    if not count:
        raise RuntimeError(
            "No auxiliary particles were found. Export Leff4fermions1Aux or "
            "Leff4fermions2Aux from the corresponding auxiliary model file "
            "before running this patch."
        )
    for start, end, new_block in reversed(replacements):
        text = text[:start] + new_block + text[end:]
    backup(path)
    path.write_text(text)
    return count


def patch_propagators(path: Path) -> None:
    text = path.read_text()
    if PROPAGATOR_MARKER not in text:
        backup(path)
        path.write_text(text.rstrip() + "\n" + PROPAGATOR_BLOCK)


def patch_antiparticle_copy(path: Path) -> None:
    """Ensure Particle.anti() retains custom propagator metadata."""
    text = path.read_text()
    if "# vSMEFT auxiliary propagator-preserving anti()" in text:
        return

    pattern = re.compile(
        r"return Particle\(-self\.pdg_code, self\.antiname, self\.name, self\.spin, newcolor, self\.mass, self\.width,\s*"
        r"self\.antitexname, self\.texname, -self\.charge, self\.line, self\.propagating, self\.goldstoneboson, \*\*outdic\)"
    )
    replacement = (
        "# vSMEFT auxiliary propagator-preserving anti()\n"
        "        return Particle(-self.pdg_code, self.antiname, self.name, self.spin, newcolor, self.mass, self.width,\n"
        "                        self.antitexname, self.texname, -self.charge, line=self.line,\n"
        "                        propagating=self.propagating,\n"
        "                        counterterm=getattr(self, 'counterterm', None),\n"
        "                        goldstoneboson=self.goldstoneboson,\n"
        "                        propagator=getattr(self, 'propagator', None), **outdic)"
    )
    text, count = pattern.subn(replacement, text, count=1)
    if count != 1:
        raise RuntimeError("Could not identify Particle.anti() in object_library.py")
    backup(path)
    path.write_text(text)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("ufo", type=Path, help="Generated UFO directory")
    args = parser.parse_args()
    ufo = args.ufo.resolve()

    required = [ufo / "particles.py", ufo / "propagators.py", ufo / "object_library.py"]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        raise SystemExit("Missing UFO files: " + ", ".join(missing))

    patch_propagators(ufo / "propagators.py")
    patch_antiparticle_copy(ufo / "object_library.py")
    count = patch_particles(ufo / "particles.py")
    print(f"Patched {count} auxiliary particle definitions in {ufo}")


if __name__ == "__main__":
    main()
