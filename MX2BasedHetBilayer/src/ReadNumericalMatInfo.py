#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 21:24:19 2019

@author: enigma
"""

from src.StructureDefinition.Hexagonal import CoordTransform
import numpy as np

def ReadNumericalMatInfo(path, mat):
    AtomicPosition = []
    CellParameters = []
    
    infile =  open('%s/2DNumericalInformation/%s_Info.dat' %(path, mat), 'r')
    line = infile.readline()
    A = float(line.split()[2])
    lines = infile.readlines()
    for i in lines:
        if ('Cell Parameters {alat' in i):
            alat = np.multiply(float(i.split('=')[1].split('}')[0]), 0.529177249)
            break
    
    with open('%s/2DNumericalInformation/%s_Info.dat' %(path, mat), 'r') as infile:
        copy = False
        for line in infile:
            if "Cell Parameters" in line:
                copy = True
            elif "Atomic Positions" in line:
                copy = False
            elif copy:
                CellParameters.append(line)
                
    with open('%s/2DNumericalInformation/%s_Info.dat' %(path, mat), 'r') as infile:
        copy = False
        for line in infile:
            if "Atomic Positions" in line:
                copy = True
            elif "Band Gap" in line:
                copy = False
            elif copy:
                AtomicPosition.append(line)
                
    
    atm = np.zeros(shape = (3,3))
    count = 0
    for i in AtomicPosition:
        if (i != ''):
            temp = i.split()[1:]
            for j in range(0, len(temp)):
                atm[count, j] = temp[j]
            count += 1
    
    cell = np.zeros(shape = (3,3))
    count = 0
    for i in CellParameters:
        if (i != ''):
            temp = i.split()
            for j in range(0, len(temp)):
                cell[count, j] = temp[j]
            count += 1
    #cell = np.divide(cell, 0.529177249)
    cell = np.multiply(cell, alat)
    CartesianCoordinate = np.array(CoordTransform.Cartesian(cell, atm))
    
    return CartesianCoordinate, cell, A
    #return AtomicPosition, CellParameters