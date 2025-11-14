# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.2.1 for Mac OS X x86 (64-bit) (March 16, 2025)
# Date: Sat 15 Nov 2025 00:02:30



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

Lambda = Parameter(name = 'Lambda',
                   nature = 'external',
                   type = 'real',
                   value = 1000.,
                   texname = '\\Lambda',
                   lhablock = 'NEWPHYSICSSCALE',
                   lhacode = [ 1 ])

VeN1 = Parameter(name = 'VeN1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = 'V_{\\text{eN1}}',
                 lhablock = 'NUMIXING',
                 lhacode = [ 1 ])

VeN2 = Parameter(name = 'VeN2',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = 'V_{\\text{eN2}}',
                 lhablock = 'NUMIXING',
                 lhacode = [ 2 ])

VeN3 = Parameter(name = 'VeN3',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = 'V_{\\text{eN3}}',
                 lhablock = 'NUMIXING',
                 lhacode = [ 3 ])

VmuN1 = Parameter(name = 'VmuN1',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'V_{\\text{muN1}}',
                  lhablock = 'NUMIXING',
                  lhacode = [ 4 ])

VmuN2 = Parameter(name = 'VmuN2',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'V_{\\text{muN2}}',
                  lhablock = 'NUMIXING',
                  lhacode = [ 5 ])

VmuN3 = Parameter(name = 'VmuN3',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'V_{\\text{muN3}}',
                  lhablock = 'NUMIXING',
                  lhacode = [ 6 ])

VtaN1 = Parameter(name = 'VtaN1',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'V_{\\text{taN1}}',
                  lhablock = 'NUMIXING',
                  lhacode = [ 7 ])

VtaN2 = Parameter(name = 'VtaN2',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'V_{\\text{taN2}}',
                  lhablock = 'NUMIXING',
                  lhacode = [ 8 ])

VtaN3 = Parameter(name = 'VtaN3',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'V_{\\text{taN3}}',
                  lhablock = 'NUMIXING',
                  lhacode = [ 9 ])

cHN1x1 = Parameter(name = 'cHN1x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cHN1x1}',
                   lhablock = 'OPERATORHN',
                   lhacode = [ 1, 1 ])

cHNe1x1 = Parameter(name = 'cHNe1x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cHNe1x1}',
                    lhablock = 'OPERATORHNe',
                    lhacode = [ 1, 1 ])

cHNe1x2 = Parameter(name = 'cHNe1x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cHNe1x2}',
                    lhablock = 'OPERATORHNe',
                    lhacode = [ 1, 2 ])

cHNe1x3 = Parameter(name = 'cHNe1x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cHNe1x3}',
                    lhablock = 'OPERATORHNe',
                    lhacode = [ 1, 3 ])

cLNH1x1 = Parameter(name = 'cLNH1x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cLNH1x1}',
                    lhablock = 'OPERATORLNH',
                    lhacode = [ 1, 1 ])

cLNH2x1 = Parameter(name = 'cLNH2x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cLNH2x1}',
                    lhablock = 'OPERATORLNH',
                    lhacode = [ 2, 1 ])

cLNH3x1 = Parameter(name = 'cLNH3x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cLNH3x1}',
                    lhablock = 'OPERATORLNH',
                    lhacode = [ 3, 1 ])

cNA1x1 = Parameter(name = 'cNA1x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cNA1x1}',
                   lhablock = 'OPERATORNA',
                   lhacode = [ 1, 1 ])

cNA2x1 = Parameter(name = 'cNA2x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cNA2x1}',
                   lhablock = 'OPERATORNA',
                   lhacode = [ 2, 1 ])

cNA3x1 = Parameter(name = 'cNA3x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cNA3x1}',
                   lhablock = 'OPERATORNA',
                   lhacode = [ 3, 1 ])

cNNH1x1 = Parameter(name = 'cNNH1x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{cNNH1x1}',
                    lhablock = 'OPERATORNNH',
                    lhacode = [ 1, 1 ])

cNZ1x1 = Parameter(name = 'cNZ1x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cNZ1x1}',
                   lhablock = 'OPERATORNZ',
                   lhacode = [ 1, 1 ])

cNZ2x1 = Parameter(name = 'cNZ2x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cNZ2x1}',
                   lhablock = 'OPERATORNZ',
                   lhacode = [ 2, 1 ])

cNZ3x1 = Parameter(name = 'cNZ3x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cNZ3x1}',
                   lhablock = 'OPERATORNZ',
                   lhacode = [ 3, 1 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.00255,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00255,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

mN1 = Parameter(name = 'mN1',
                nature = 'external',
                type = 'real',
                value = 300.,
                texname = '\\text{mN1}',
                lhablock = 'MASS',
                lhacode = [ 9900012 ])

mN2 = Parameter(name = 'mN2',
                nature = 'external',
                type = 'real',
                value = 500.,
                texname = '\\text{mN2}',
                lhablock = 'MASS',
                lhacode = [ 9900014 ])

mN3 = Parameter(name = 'mN3',
                nature = 'external',
                type = 'real',
                value = 1000.,
                texname = '\\text{mN3}',
                lhablock = 'MASS',
                lhacode = [ 9900016 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WN1 = Parameter(name = 'WN1',
                nature = 'external',
                type = 'real',
                value = 0.303,
                texname = '\\text{WN1}',
                lhablock = 'DECAY',
                lhacode = [ 9900012 ])

WN2 = Parameter(name = 'WN2',
                nature = 'external',
                type = 'real',
                value = 1.5,
                texname = '\\text{WN2}',
                lhablock = 'DECAY',
                lhacode = [ 9900014 ])

WN3 = Parameter(name = 'WN3',
                nature = 'external',
                type = 'real',
                value = 12.3,
                texname = '\\text{WN3}',
                lhablock = 'DECAY',
                lhacode = [ 9900016 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

PMNS1x1 = Parameter(name = 'PMNS1x1',
                    nature = 'internal',
                    type = 'real',
                    value = '1',
                    texname = '\\text{PMNS1x1}')

PMNS1x2 = Parameter(name = 'PMNS1x2',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{PMNS1x2}')

PMNS1x3 = Parameter(name = 'PMNS1x3',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{PMNS1x3}')

PMNS1x4 = Parameter(name = 'PMNS1x4',
                    nature = 'internal',
                    type = 'real',
                    value = 'VeN1',
                    texname = '\\text{PMNS1x4}')

PMNS1x5 = Parameter(name = 'PMNS1x5',
                    nature = 'internal',
                    type = 'real',
                    value = 'VeN2',
                    texname = '\\text{PMNS1x5}')

PMNS1x6 = Parameter(name = 'PMNS1x6',
                    nature = 'internal',
                    type = 'real',
                    value = 'VeN3',
                    texname = '\\text{PMNS1x6}')

PMNS2x1 = Parameter(name = 'PMNS2x1',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{PMNS2x1}')

PMNS2x2 = Parameter(name = 'PMNS2x2',
                    nature = 'internal',
                    type = 'real',
                    value = '1',
                    texname = '\\text{PMNS2x2}')

PMNS2x3 = Parameter(name = 'PMNS2x3',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{PMNS2x3}')

PMNS2x4 = Parameter(name = 'PMNS2x4',
                    nature = 'internal',
                    type = 'real',
                    value = 'VmuN1',
                    texname = '\\text{PMNS2x4}')

PMNS2x5 = Parameter(name = 'PMNS2x5',
                    nature = 'internal',
                    type = 'real',
                    value = 'VmuN2',
                    texname = '\\text{PMNS2x5}')

PMNS2x6 = Parameter(name = 'PMNS2x6',
                    nature = 'internal',
                    type = 'real',
                    value = 'VmuN3',
                    texname = '\\text{PMNS2x6}')

PMNS3x1 = Parameter(name = 'PMNS3x1',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{PMNS3x1}')

PMNS3x2 = Parameter(name = 'PMNS3x2',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{PMNS3x2}')

PMNS3x3 = Parameter(name = 'PMNS3x3',
                    nature = 'internal',
                    type = 'real',
                    value = '1',
                    texname = '\\text{PMNS3x3}')

PMNS3x4 = Parameter(name = 'PMNS3x4',
                    nature = 'internal',
                    type = 'real',
                    value = 'VtaN1',
                    texname = '\\text{PMNS3x4}')

PMNS3x5 = Parameter(name = 'PMNS3x5',
                    nature = 'internal',
                    type = 'real',
                    value = 'VtaN2',
                    texname = '\\text{PMNS3x5}')

PMNS3x6 = Parameter(name = 'PMNS3x6',
                    nature = 'internal',
                    type = 'real',
                    value = 'VtaN3',
                    texname = '\\text{PMNS3x6}')

numass1x1 = Parameter(name = 'numass1x1',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass1x1}')

numass1x2 = Parameter(name = 'numass1x2',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass1x2}')

numass1x3 = Parameter(name = 'numass1x3',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass1x3}')

numass1x4 = Parameter(name = 'numass1x4',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass1x4}')

numass1x5 = Parameter(name = 'numass1x5',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass1x5}')

numass1x6 = Parameter(name = 'numass1x6',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass1x6}')

numass2x1 = Parameter(name = 'numass2x1',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass2x1}')

numass2x2 = Parameter(name = 'numass2x2',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass2x2}')

numass2x3 = Parameter(name = 'numass2x3',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass2x3}')

numass2x4 = Parameter(name = 'numass2x4',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass2x4}')

numass2x5 = Parameter(name = 'numass2x5',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass2x5}')

numass2x6 = Parameter(name = 'numass2x6',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass2x6}')

numass3x1 = Parameter(name = 'numass3x1',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass3x1}')

numass3x2 = Parameter(name = 'numass3x2',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass3x2}')

numass3x3 = Parameter(name = 'numass3x3',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass3x3}')

numass3x4 = Parameter(name = 'numass3x4',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass3x4}')

numass3x5 = Parameter(name = 'numass3x5',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass3x5}')

numass3x6 = Parameter(name = 'numass3x6',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass3x6}')

numass4x1 = Parameter(name = 'numass4x1',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass4x1}')

numass4x2 = Parameter(name = 'numass4x2',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass4x2}')

numass4x3 = Parameter(name = 'numass4x3',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass4x3}')

numass4x4 = Parameter(name = 'numass4x4',
                      nature = 'internal',
                      type = 'real',
                      value = 'mN1',
                      texname = '\\text{numass4x4}')

numass4x5 = Parameter(name = 'numass4x5',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass4x5}')

numass4x6 = Parameter(name = 'numass4x6',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass4x6}')

numass5x1 = Parameter(name = 'numass5x1',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass5x1}')

numass5x2 = Parameter(name = 'numass5x2',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass5x2}')

numass5x3 = Parameter(name = 'numass5x3',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass5x3}')

numass5x4 = Parameter(name = 'numass5x4',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass5x4}')

numass5x5 = Parameter(name = 'numass5x5',
                      nature = 'internal',
                      type = 'real',
                      value = 'mN2',
                      texname = '\\text{numass5x5}')

numass5x6 = Parameter(name = 'numass5x6',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass5x6}')

numass6x1 = Parameter(name = 'numass6x1',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass6x1}')

numass6x2 = Parameter(name = 'numass6x2',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass6x2}')

numass6x3 = Parameter(name = 'numass6x3',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass6x3}')

numass6x4 = Parameter(name = 'numass6x4',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass6x4}')

numass6x5 = Parameter(name = 'numass6x5',
                      nature = 'internal',
                      type = 'real',
                      value = '0',
                      texname = '\\text{numass6x5}')

numass6x6 = Parameter(name = 'numass6x6',
                      nature = 'internal',
                      type = 'real',
                      value = 'mN3',
                      texname = '\\text{numass6x6}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

cNB1x1 = Parameter(name = 'cNB1x1',
                   nature = 'internal',
                   type = 'real',
                   value = 'cNA1x1*cw - cNZ1x1*sw',
                   texname = '\\text{cNB1x1}')

cNB2x1 = Parameter(name = 'cNB2x1',
                   nature = 'internal',
                   type = 'real',
                   value = 'cNA2x1*cw - cNZ2x1*sw',
                   texname = '\\text{cNB2x1}')

cNB3x1 = Parameter(name = 'cNB3x1',
                   nature = 'internal',
                   type = 'real',
                   value = 'cNA3x1*cw - cNZ3x1*sw',
                   texname = '\\text{cNB3x1}')

cNW1x1 = Parameter(name = 'cNW1x1',
                   nature = 'internal',
                   type = 'real',
                   value = 'cNZ1x1*cw + cNA1x1*sw',
                   texname = '\\text{cNW1x1}')

cNW2x1 = Parameter(name = 'cNW2x1',
                   nature = 'internal',
                   type = 'real',
                   value = 'cNZ2x1*cw + cNA2x1*sw',
                   texname = '\\text{cNW2x1}')

cNW3x1 = Parameter(name = 'cNW3x1',
                   nature = 'internal',
                   type = 'real',
                   value = 'cNZ3x1*cw + cNA3x1*sw',
                   texname = '\\text{cNW3x1}')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gN = Parameter(name = 'gN',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_N')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vev',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vev',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vev',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vev',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vev',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vev',
                texname = '\\text{yup}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

