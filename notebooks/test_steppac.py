# numpy
import numpy as np
from numpy import pi, sqrt, log, log10, power, exp

#scipy
from scipy.interpolate import interp1d

# matplotlib
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import rc
from matplotlib.lines import Line2D

# other
import os
import sys

from tqdm import tqdm

# current directory
current_dir = os.getcwd()

# include paths from above
sys.path.insert(0, '../')


# import classy module
from classy import Class

common_settings = {'omega_b':0.0223828,
                   'omega_dm_tot':0.1201075,
                   # 'H0':67.32117,
                   '100*theta_s':1.04179712,
                   'A_s':2.100549e-09,
                   'n_s':0.9660499,
                   'tau_reio':0.05430842,
                   'N_ur':2.046,
                   'N_ncdm':1,
                   'm_ncdm':0.06,
                   'T_ncdm':0.7137658555036082,
                   # 'YHe':0.2454006,
                   'YHe':'BBN',
                   'output':'tCl,pCl,lCl,mPk',
                   'lensing':'yes',
                   'P_k_max_1/Mpc':30.0,
                   'non linear':'halofit',
                   'k_output_values':'0.01,0.1,1.,2.'
                  }

verbosity = {'input_verbose':2,
             'background_verbose':2,
             'thermodynamics_verbose':2,
             'perturbations_verbose':2
            }




# create instance of the class "Class"
LCDM = Class()
# pass input parameters
LCDM.set(common_settings)
LCDM.set(verbosity)
# run class
LCDM.compute()





pacdm_params = {'omega_dm_tot':0.120790370827,
                'f_pacdm':0.03,
                'N_IR':0.05,
                
                # Manuel's plot
                # 'r_g':0.,
                # 'a_tr':0.99,
                # 'GH_ratio':100.,
                # 'a_ref_pacdr':1.e-8
                
                # Taewook's plot
                'g_IR':2.,
                'g_UV':5.5,
                'a_tr':0.0909090909091,
                'm_pacdm':10.,
                'alpha_pac':1.e-7
               }

PACDM = Class()

PACDM.set(common_settings)
PACDM.set(pacdm_params)
PACDM.set(verbosity)

PACDM.compute()






spartacous_params = {'omega_dm_tot':0.121063122941,
                  'f_pacdm':0.03,
                  'm_pacdm':10.,
                  'N_IR':0.05,
                  'g_IR':2.,
                  'g_UV':5.5,
                  'a_tr':3.16e-5,#log10(zt) ~= 4.5
                  
                  # Manuel's plot:
                  # 'GH_ratio':100.,
                  # 'a_ref_pacdr':1.e-8
                  
                  # Taewook's plot:
                  'alpha_pac':1.e-7
                 }


spartacous_params = {'omega_dm_tot':0.121063122941,
                  'f_pacdm':0.03,
                  'm_pacdm':10.,
                  'N_IR':0.05,
                  'g_IR':2.,
                  'g_UV':5.5,
                  'a_tr':3.16e-5,#log10(zt) ~= 4.5
                  
                  # Manuel's plot:
                  # 'GH_ratio':100.,
                  # 'a_ref_pacdr':1.e-8
                  
                  # Taewook's plot:
                  'alpha_pac':1.e-7
                 }





h = LCDM.h()

# Getting P(k) at redhsift z=0

kk = np.logspace(-5, log10(30.), 300) # Nadler's values for k
LPk = [] # P(k) in (Mpc/h)**3
PPk = []
SPk = []

for k in kk:
    Lh = LCDM.h()
    Ph = PACDM.h()
    Sh = STEPPAC.h()
    
    LPk.append(LCDM.pk_lin(k*Lh, 0.)*Lh**3) # function .pk(k,z)
    PPk.append(PACDM.pk_lin(k*Ph, 0.)*Ph**3)
    SPk.append(STEPPAC.pk_lin(k*Sh, 0.)*Sh**3)
    

LPk=np.array(LPk)
PPk=np.array(PPk)
SPk=np.array(SPk)






plt.plot(kk, PPk/LPk, label="PAcDM")
plt.plot(kk, SPk/LPk, label="SPartAcous")

plt.xscale('log');
plt.ylabel("T^2(k)");plt.xlabel("k [h/Mpc]");
plt.legend();
plt.title("f_pacdm = 3%, N_IR = 0.05 (log10 z_t = 4.5)");
plt.savefig("./test_Pk.pdf");
