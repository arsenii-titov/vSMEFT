# FeynRules and UFO models for <span>$\nu$</span>SMEFT

[![arXiv](https://img.shields.io/badge/arXiv-2511.10733-B31B1B?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.10733)
[![Published version](https://img.shields.io/badge/Comput.%20Phys.%20Commun.-331%20%282027%29%20110485-0077B5?style=flat-square)](https://doi.org/10.1016/j.cpc.2026.110485)

The <span>$\nu$</span>SMEFT (also known as NSMEFT, SMNEFT or <span>$N_R$</span>SMEFT) is the effective field theory of the Standard Model (SM) extended by right-handed neutrinos, <span>$N_R$</span>. This repository provides FeynRules and UFO implementations of the baryon-number-conserving dimension-five and dimension-six operators involving <span>$N_R$</span>, together with the renormalisable SM + <span>$N_R$</span> Lagrangian.

Version 2.0 extends the original Higgs–<span>$N_R$</span> implementation to include four-fermion operators containing either one or two <span>$N_R$</span> fields.

## Repository contents

### FeynRules models

The [`FeynRules_models`](FeynRules_models) directory contains:

| File | Contents |
|---|---|
| [`SM_v_Majorana.fr`](FeynRules_models/SM_v_Majorana.fr) | SM implementation with Majorana neutrinos |
| [`vSM.fr`](FeynRules_models/vSM.fr) | Renormalisable SM + <span>$N_R$</span> model |
| [`vSMEFT_2-fermions_Higgs-N.fr`](FeynRules_models/vSMEFT_2-fermions_Higgs-N.fr) | Dimension-five and dimension-six Higgs–<span>$N_R$</span> operators |
| [`vSMEFT_4-fermions_single-N.fr`](FeynRules_models/vSMEFT_4-fermions_single-N.fr) | Direct four-fermion operators with one <span>$N_R$</span> |
| [`vSMEFT_4-fermions_pair-N.fr`](FeynRules_models/vSMEFT_4-fermions_pair-N.fr) | Direct four-fermion operators with two <span>$N_R$</span> fields |
| [`vSMEFT_4-fermions_single-N_aux.fr`](FeynRules_models/vSMEFT_4-fermions_single-N_aux.fr) | Auxiliary-field implementation of the single-<span>$N_R$</span> operators |
| [`vSMEFT_4-fermions_pair-N_aux.fr`](FeynRules_models/vSMEFT_4-fermions_pair-N_aux.fr) | Auxiliary-field implementation of the pair-<span>$N_R$</span> operators |
| [`vSMEFT.fr`](FeynRules_models/vSMEFT.fr) | Complete model combining the Higgs–<span>$N_R$</span> and both auxiliary four-fermion sectors |

The direct four-fermion implementations are intended for analytic calculations and checks in FeynRules. For MadGraph simulations, the corresponding auxiliary-field implementations should be used: they replace each four-fermion contact interaction involving Majorana fermions by three-point interactions with non-propagating auxiliary fields.

### Mathematica notebooks

The [`Mathematica_notebooks`](Mathematica_notebooks) directory contains a notebook for each individual sector and for the complete model. They illustrate how to load the FeynRules files, perform standard consistency checks, calculate vertices and export the corresponding UFO model with `WriteUFO`.

### UFO models

The [`UFO_models`](UFO_models) directory contains the following ready-to-use models:

| UFO model | Included interactions |
|---|---|
| [`vSMEFT_2-fermions_Higgs-N_UFO`](UFO_models/vSMEFT_2-fermions_Higgs-N_UFO) | Higgs–<span>$N_R$</span> sector |
| [`vSMEFT_4-fermions_single-N_aux_UFO`](UFO_models/vSMEFT_4-fermions_single-N_aux_UFO) | Single-<span>$N_R$</span> four-fermion sector |
| [`vSMEFT_4-fermions_pair-N_aux_UFO`](UFO_models/vSMEFT_4-fermions_pair-N_aux_UFO) | Pair-<span>$N_R$</span> four-fermion sector |
| [`vSMEFT_UFO`](UFO_models/vSMEFT_UFO) | Complete model |

The distributed auxiliary UFO models have already been patched as described below and can be imported directly into MadGraph5_aMC@NLO.

## Regenerating an auxiliary UFO

FeynRules does not generate the momentum-independent auxiliary propagators required by this implementation automatically. After using `WriteUFO` to export a model containing `Leff4fermions1Aux`, `Leff4fermions2Aux`, or both, run:

```bash
python3 patch_vSMEFT_aux_ufo.py /absolute/path/to/generated_UFO
```

The included [`patch_vSMEFT_aux_ufo.py`](patch_vSMEFT_aux_ufo.py) script:

- installs the constant scalar and vector auxiliary propagators;
- marks the auxiliary particles as unavailable as external states;
- sets their mass parameter to `Lambda`, which fixes the EFT normalisation and is not a pole mass;
- creates `*.pre_aux_patch` backups before the first modification.

The operation is idempotent, so running it more than once is safe. It is not necessary to run it on the UFO directories supplied in this repository.

## Using the models with MadGraph5_aMC@NLO

Copy the desired UFO directory into the `models` directory of MadGraph5_aMC@NLO, or import it using its absolute path. For example, after copying the complete model:

```text
MG5_aMC> import model vSMEFT_UFO
MG5_aMC> generate e+ e- > n1 n1
MG5_aMC> output ee_to_NN
MG5_aMC> launch
> set mN1 10
> set Lambda 1000
> set ceN1x1 1
```

Masses and `Lambda` are specified in GeV. Wilson coefficients vanish by default. The complete list of parameters and their MadGraph names is available in each UFO model's `parameters.py` file and in the parameter card generated by MadGraph.

## Citation and credit

The model files build on the implementations developed in Refs. [1–3] and are described in Ref. [4]. If you use these files, please cite the references relevant to the sectors used in your study.

The auxiliary-field reformulation and its software implementation were developed with assistance from OpenAI Codex; the author reviewed and validated the resulting code.

## References

1. <a id="ref2019"></a> J. M. Butterworth, M. Chala, C. Englert, M. Spannowsky and A. Titov, *Higgs phenomenology as a probe of sterile neutrinos*, [Phys. Rev. D **100** (2019) 115019](https://doi.org/10.1103/PhysRevD.100.115019) [[arXiv:1909.04665](https://arxiv.org/abs/1909.04665)].

2. <a id="ref2021"></a> G. Cottin, J. C. Helo, M. Hirsch, A. Titov and Z. S. Wang, *Heavy neutral leptons in effective field theory and the high-luminosity LHC*, [JHEP **09** (2021) 039](https://doi.org/10.1007/JHEP09%282021%29039) [[arXiv:2105.13851](https://arxiv.org/abs/2105.13851)].

3. <a id="ref2022"></a> R. Beltrán, G. Cottin, J. C. Helo, M. Hirsch, A. Titov and Z. S. Wang, *Long-lived heavy neutral leptons at the LHC: four-fermion single-*<span>$N_R$</span> *operators*, [JHEP **01** (2022) 044](https://doi.org/10.1007/JHEP01%282022%29044) [[arXiv:2110.15096](https://arxiv.org/abs/2110.15096)].

4. <a id="ref2025"></a> A. Titov, *FeynRules and UFO models for* <span>$\nu$</span>*SMEFT: operators of dimensions five and six*, [Comput. Phys. Commun. **331** (2027) 110485](https://doi.org/doi:10.1016/j.cpc.2026.110485) [[arXiv:2511.10733](https://arxiv.org/abs/2511.10733)].

## License

This repository is distributed under the terms of the [MIT License](LICENSE).
