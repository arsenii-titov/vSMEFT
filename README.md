**FeynRules and UFO model files for the vSMEFT** 

vSMEFT is the effective field theory (EFT) of the Standard Model (SM) extended with right-handed (RH) neutrinos, $N_R$. 

The FeynRules file `vSMEFT_Higgs-N.fr` extends the default SM model file and the HeavyN model file with dimension-5 and dimension-6 Higgs-<span>$N_R$</span> interactions. 
In `SM_v_Majorana.fr` neutrinos are set to be Majorana (SelfConjugate -> True). This is the only difference with respect to the default SM model file `SM.fr` supplied with FeynRules.

The Mathematica notebook `vSMEFT_Higgs-N_UFO.nb` loads and merges the FeynRules models `SM_v_Majorana.fr` and `vSMEFT_Higgs-N.fr`, performs a number of sanity checks, computes Feynman rules and generates the corresponding UFO model `vSMEFT_Higgs-N_UFO` (also available as a zip file `vSMEFT_Higgs-N_UFO.zip`).
