#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 19:25:39 2019

@author: enigma
"""

import numpy as np

def GetKpointXCordinates(BandStructureDOTOutFile, IntersectionPoints, no_HighSymmetryPoints, nks):
    kpoint = np.zeros((no_HighSymmetryPoints, 1), dtype = float, order = 'C')
    count = 0
    infile = open(BandStructureDOTOutFile, 'rt')
    for line in infile:
        temp = line.split()
        if (len(temp) > 1 and temp[0] == 'high-symmetry'):
            kpoint[count][0] = temp[7]
            count = count + 1
    step = np.zeros((len(kpoint)-1, 1), dtype = float, order = 'C')
    for i in range(0, len(kpoint)):
        if (i == len(step)):
            break
        else:
            step[i][0] = np.subtract(kpoint[i+1][0], kpoint[i][0])
            step[i][0] = np.divide(step[i][0], IntersectionPoints)
    
    k = np.zeros((len(kpoint)-1, IntersectionPoints), dtype = float, order = 'C')
    
    for i in range(0, len(kpoint)):
        if (i == len(kpoint)-1):
            break
        else:
            k[i] = np.arange(kpoint[i][0], kpoint[i+1][0], step[i][0], dtype = float)
    
    temp = np.ravel(k, order = 'C')
    #value = temp[len(temp)-1] + step[len(step)-1]
    #temp[i][0] = value
    kpointxcoordinates = np.append(temp, np.add(temp[len(temp)-1], step[len(step)-1]), axis = 0)
    
    return kpointxcoordinates
    
    