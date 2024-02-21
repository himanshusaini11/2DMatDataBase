#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 18:29:50 2019

@author: enigma
"""

import numpy as np

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

def GetKpointXCordinates(BandStructureDOTOutFile, IntersectionPoints, no_HighSymmetryPoints, nks):
    kpoint = np.zeros((no_HighSymmetryPoints, 1), dtype = float, order = 'C')
    count = 0
    infile = open(BandStructureDOTOutFile, 'rt')
    for line in infile:
        temp = line.split()
        if (len(temp) > 1 and temp[0] == 'high-symmetry'):
            kpoint[count][0] = temp[7]
            count = count + 1
    print (kpoint)
    step = np.zeros((len(kpoint)-1, 1), dtype = float, order = 'C')
    
    for i in range(0, len(kpoint)):
        if (i == len(step)):
            break
        else:
            step[i][0] = np.subtract(kpoint[i+1][0], kpoint[i][0])
            step[i][0] = np.divide(step[i][0], IntersectionPoints)
    print (step)
    k = np.zeros((len(kpoint)-1, IntersectionPoints), dtype = float, order = 'C')
    print (k.shape)
        
    for i in range(0, len(kpoint)):
        if (i == len(kpoint)-1):
            break
        else:
            k[i] = np.arange(kpoint[i][0], kpoint[i+1][0], step[i][0], dtype = float)
    
    temp = np.ravel(k, order = 'C')
    kpointxcoordinates = np.append(temp, np.add(temp[len(temp)-1], step[len(step)-1]), axis = 0)
    
    return kpointxcoordinates, kpoint