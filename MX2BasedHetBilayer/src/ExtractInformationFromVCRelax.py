#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:39:40 2019

@author: enigma
"""

def ExtractCellInformation(path, DataBaseFolder, MatName):
    readpath = path + '/%s/%s' %(DataBaseFolder, MatName)
    FinalCoordinate = []
    with open(readpath + '/Relax.out') as infile:
        copy = False
        for line in infile:
            if line.strip() == "Begin final coordinates":
                copy = True
            elif line.strip() == "End final coordinates":
                copy = False
            elif copy:
                FinalCoordinate.append(line)
    infile.close()
    
    return FinalCoordinate
    
def Information(path, DataBaseFolder, MatName):
    import numpy as np
    #import os
    #path = os.getcwd()
    #DataBaseFolder = 'VCRelaxDataBase'
    #MatName = 'MoS2'
    
    CellInformation = ExtractCellInformation(path, DataBaseFolder, MatName)
    for i in CellInformation:
        temp = i.split()
        if (temp[2] == 'volume'):
            volume = float(temp[7])
        elif (temp[0] == 'density'):
            density = float(temp[2])
            break
            
    #print (len(CellInformation))
    CellParameters = []
    for i in range(0, len(CellInformation)):
        if (i == 4 or i == 5 or i == 6):
            CellParameters.append(CellInformation[i])
            
    infile = open('CellParameters.dat', 'w')
    count = 0
    for i in CellParameters:
        infile.write(i)
        temp = i.split()
        if (count == 0):
            A = np.array(temp, dtype = float)
        elif (count == 1):
            B = np.array(temp, dtype = float)
        else:
            C = np.array(temp, dtype = float)
        count += 1
        #print (A)   
    infile.close()
    
    AtomicCoordinates = []
    for i in range(9, len(CellInformation)):
        AtomicCoordinates.append(CellInformation[i])
            
    infile = open('AtomicCoordinates.dat', 'w')
    for i in AtomicCoordinates:
        infile.write(i)
        
    infile.close()
    
    return volume, density, AtomicCoordinates, CellParameters