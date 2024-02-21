#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 10:29:38 2019

@author: enigma
"""

from src.MatList import MatListData
import os
import numpy as np

MatName = MatListData()

def GetEigenValues(BandsDatFile):
    eigenfile = open(BandsDatFile, 'r')
    header = eigenfile.readline()
    nbnd = int(header.split(',')[0].split('=')[1])
    nks = int(header.split(',')[1].split('=')[1].split('/')[0])
    eigenvalues = np.zeros((nks, nbnd), dtype = float)
    for i in range(nks):
        header = eigenfile.readline()
        count = 0
        for j in range(nbnd//10+1):
            header = eigenfile.readline()
            for k in range(len(header.split())):
                eigenvalues[i][count] = header.split()[k]
                count = count + 1
    return nbnd, nks, eigenvalues

def BandGap(path, mat):
    
    pathBandsDatFile = path + '/MaterialsDataBase/ElectronicProperties/' + mat + '/Analysis/BandStructure/'
    pathSCFOutFile = path + '/MaterialsDataBase/ElectronicProperties/' + mat + '/SCF/'
    BandsDatFile = 'Bands.dat'
    SCFOutFile = 'SCF.out'
    
    os.chdir(pathSCFOutFile)
    infile = open(SCFOutFile, 'rt')
    for line in infile.readlines():
        if ('     the Fermi energy is' in line):
            FermiEnergy = line.split()
            FermiEnergy = float(FermiEnergy[4])
            break
    os.chdir(path)
    
    os.chdir(pathBandsDatFile)
    nbnd, nks, eigenvalues = GetEigenValues(BandsDatFile)
    os.chdir(path)
    
    #eigenvalues = eigenvalues - FermiEnergy
    CB = []
    VB = []
    for i in range(0, nks):
        for j in range(0, nbnd):
            if (eigenvalues[i][j] > FermiEnergy):
                CB.append(eigenvalues[i][j])
            elif (eigenvalues[i][j] < FermiEnergy):
                VB.append(eigenvalues[i][j])
                
    CB = np.array(CB)
    VB = np.array(VB)
    
    BandGap = np.subtract(CB.min(), VB.max())
    
    return BandGap, VB.max(), CB.min(), FermiEnergy