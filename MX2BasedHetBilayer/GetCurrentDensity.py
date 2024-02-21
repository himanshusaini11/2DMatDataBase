#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 16:55:21 2019

@author: enigma
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from src.GetAbsorption import OpticalProperties
import os
import matplotlib.pyplot as plt
import scipy.integrate as integrate

def AM15G():
    df = pd.read_excel('astmg173.xls', header = 1)
    arr = np.array(df)
    
    return arr

Spectrum = AM15G()
PhotonFlux = ((Spectrum[:, 2] * Spectrum[:, 0]) / (1.24/Spectrum[:, 0] * 1000 * 1.6E-19)) / 10000 # unit #of photons/cm^2.sec
PhotonWavelength = Spectrum[:, 0]
PhotonEnergy = 1.24/Spectrum[:, 0] * 1000

f = interpolate.interp1d(PhotonEnergy, PhotonFlux, bounds_error = False, fill_value=0)
EnergyInp = np.linspace(0, 10, num = 3001, endpoint = True)
PhotonFluxInp = f(EnergyInp)

path = os.getcwd()
opt = OpticalProperties(path, 'MoS2-WSe2', 'x', '2D', 30E-10)
Absorbance = opt.Absorbance()
real, imag = opt.DielectricFunction()
Energy = imag[:, 0]

f = interpolate.interp1d(Energy, Absorbance, bounds_error = False, fill_value=0)
AbsorbanceInp = f(EnergyInp)
AJph = np.multiply((AbsorbanceInp), (PhotonFluxInp))
Eg = EnergyInp.tolist().index(0.55)
Emax = EnergyInp.tolist().index(np.max(EnergyInp))

AJph1 = AJph[Eg:Emax]
Ex = EnergyInp[Eg:Emax]

CurrentDensity = integrate.cumtrapz(AJph1, Ex, initial = 0) * 1.60217662E-19
CurrentDensity = np.max(CurrentDensity) * 1000
#plt.plot(Ex, CurrentDensity, 'ro')
#plt.show()




#plt.plot(xnew, ynew, '-', xnew, yynew, 'o')
#plt.show()

