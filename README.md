# FeynRules and UFO model files for <span>$\nu$</span>SMEFT

The <span>$\nu$</span>SMEFT (also known as NSMEFT, SMNEFT, <span>$N_R$</span>SMEFT) is the effective field theory (EFT) of the Standard Model (SM) extended with right-handed (RH) neutrinos, $N_R$. 

The FeynRules file `vSMEFT_Higgs-N.fr` extends the default [SM](https://feynrules.irmp.ucl.ac.be/wiki/StandardModel) model file and the [HeavyN](https://feynrules.irmp.ucl.ac.be/wiki/HeavyN) model file with **dimension-5 and dimension-6 Higgs-<span>$N_R$</span> interactions**. 
In `SM_v_Majorana.fr` neutrinos are set to be Majorana (SelfConjugate -> True). This is the only difference with respect to the default SM model file `SM.fr` supplied with FeynRules.

The Mathematica notebook `vSMEFT_Higgs-N_UFO.nb` loads and merges the FeynRules models `SM_v_Majorana.fr` and `vSMEFT_Higgs-N.fr`, performs a number of sanity checks, computes Feynman rules and generates the corresponding UFO model `vSMEFT_Higgs-N_UFO` (also available as a zip file `vSMEFT_Higgs-N_UFO.zip`). The latter can be used to perform simulations with MadGraph5_aMC@NLO.

The present model files are largely based on those originally developed in Ref. [1](#ref2019). 
Their description is provided in Ref. [2](#ref2025). 
If you use the model files, please cite these references.


## References

1. <a id="ref2019"></a> J. M. Butterworth, M. Chala, C. Englert, M. Spannowsky and A. Titov,
*Higgs phenomenology as a probe of sterile neutrinos*,
[Phys. Rev. D **100** (2019) 115019](https://doi.org/10.1103/PhysRevD.100.115019) [[arXiv:1909.04665](https://arxiv.org/abs/1909.04665)].
  
2. <a id="ref2025"></a> A. Titov, 
*FeynRules and UFO model files for* <span>$\nu$</span>*SMEFT: Higgs-*<span>$N_R$</span> *operators of dimensions five and six*, 
[arXiv:2511.XXXXX](https://arxiv.org/abs/2511.XXXXX).
