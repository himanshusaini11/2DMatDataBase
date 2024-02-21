#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 19:53:22 2019

@author: enigma
"""

import os

def MaterialInformation(A, B, C, alpha, beta, gamma, unitcellVol, density, celldm1, cellPar, AtomicPos, bandgap, VBM_Vacc, CBM_Vacc, WorkFunction, LowdinCharge):
    info = str("""A = %.4f Angstrom
B = %.4f Angstrom
C = %.4f Angtrom
alpha = %.2f Degree
beta = %.2f Degree
gamma = %.2f Degree

Unit Cell Volume = %.9f Angs^3
Density = %.9f g/cm^3
Cell Parameters {alat=%.10f}
%s
Atomic Positions {crystal} 
%s

Band Gap = %.4f eV
Band Edge with respect to vacuum: Ev = 0 eV
VBM = %.4f eV
CBM = %.4f eV
Work Function = %.4f

Lowdin Charges:
    %s""" %(A, B, C, alpha, beta, gamma, unitcellVol, density, celldm1, cellPar, AtomicPos, bandgap, VBM_Vacc, CBM_Vacc, WorkFunction, LowdinCharge))
    
    return info

def Directory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' + directory)
        
def WriteInfoFile(path, filename, value):
    data_base = 'MaterialsDataBase/NumericalInformation'
    Directory(path + '/' + data_base)
    dbpath = path + '/' + data_base
    
    os.chdir(dbpath)
    infile = open(filename, 'w')
    infile.write(value)
    infile.close
    os.chdir(path)

def WriteMatInfo(path, mat, A, B, C, alpha, beta, gamma, unitcellVol, density, celldm1, cellPar, AtomicPos, bandgap, VBM_Vacc, CBM_Vacc, WorkFunction, LowdinCharge):
    info = MaterialInformation(A, B, C, alpha, beta, gamma, unitcellVol, density, celldm1, cellPar, AtomicPos, bandgap, VBM_Vacc, CBM_Vacc, WorkFunction, LowdinCharge)
    WriteInfoFile(path, str('%s_Info.dat' %mat), info)
    