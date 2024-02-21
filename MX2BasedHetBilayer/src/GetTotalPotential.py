#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 19:06:07 2019

@author: enigma
"""

import numpy as np
import os
def Potential(path, mat):
    pathPotentialDatFile = path + '/MaterialsDataBase/ElectronicProperties/' + mat + '/Analysis/TotalPotential/'
    pathSCFOutFile = path + '/MaterialsDataBase/ElectronicProperties/' + mat + '/SCF/'
    PotentialFile = 'avg.dat'
    SCFOutFile = 'SCF.out'
    
    os.chdir(pathSCFOutFile)
    infile = open(SCFOutFile, 'rt')
    for line in infile.readlines():
        if ('     the Fermi energy is' in line):
            FermiEnergy = line.split()
            FermiEnergy = float(FermiEnergy[4])
            break
    os.chdir(path)
    os.chdir(pathPotentialDatFile)
    #Potential = np.fromfile(PotentialFile, dtype = float)
    Potential = np.loadtxt(PotentialFile)
    os.chdir(path)
    
    #eigenvalues = eigenvalues - FermiEnergy
    #CB = []
    #VB = []
    #for i in range(0, nks):
    #    for j in range(0, nbnd):
    #        if (eigenvalues[i][j] > 0):
    #            CB.append(eigenvalues[i][j])
    #        else:
    #            VB.append(eigenvalues[i][j])
    #            
    #CB = np.array(CB)
    #VB = np.array(VB)
    # 
    # BandGap = np.subtract(CB.min(), VB.max())
    
    return Potential