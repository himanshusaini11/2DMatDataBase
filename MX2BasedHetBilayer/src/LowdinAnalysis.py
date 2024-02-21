#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:24:04 2019

@author: enigma
"""

def LowdinCharge(path, mat):
    readpath = str("%s/MaterialsDataBase/ElectronicProperties/%s/Analysis/ProjectedDensityOfStates" %(path, mat))
    with open('%s/ProjectedDensityOfStates.out' %readpath, 'r') as infile, open('Lowdin.dat', 'w') as outfile:
        copy = False
        for line in infile:
            if "Lowdin Charges:" in line:
                copy = True
            elif "PROJWFC" in line:
                copy = False
            elif copy:
                outfile.write(line)
    infile = open ('Lowdin.dat', 'r')
    lowdin = infile.read()
    infile.close()
    
    return lowdin

