#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 20:11:05 2019

@author: enigma
"""

import os
import numpy as np

def ExtractTE(path, filename):
    os.chdir(path)
    TotalEnergy = 0
    with open(filename, 'rt') as infile:
        for line in infile:
            string = "!    total energy              ="
            temp = string in line
            if (temp == True):
                TotalEnergy = line.split()
                TotalEnergy = float(TotalEnergy[4])
                break
    infile.close()
    
    return TotalEnergy

def ExtractAlat(path, filename):
    alat = 0
    os.chdir(path)
    with open(filename, 'rt') as infile:    
        for line in infile:
            #string = "celldm(1)"
            string = "unit-cell volume          ="
            temp = string in line
            if (temp == True):
                alat = line.split()
                alat = float(alat[3])
                break
    infile.close()
    
    return alat

def Directory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' + directory)

def WriteData(path, mat, alat_range):
    #lattice = float(startalat)
    newpath = str(path + "/EOSDataBase" + "/" + "%s" %mat)
    
    #alat_range = np.linspace(lattice - 1.5, lattice + 1.5, 20)
    for j in range(0, len(alat_range)):
        outputfile = str("%s_%.2f.out" %(mat, alat_range[j]))
        TotalEnergy = ExtractTE(newpath, outputfile)
        Lattice = ExtractAlat(newpath, outputfile)
        os.chdir(path)
        Directory(path + '/EOSData')
        os.chdir(path + '/EOSData')
        if (os.path.isfile('./%s_Lattice.dat' %mat) == True):
            infile = open('%s_Lattice.dat' %mat, "a")
            if (TotalEnergy != 0):
                infile.write("%f\t%f \n" %(Lattice, TotalEnergy))
            infile.close()
        else:
            infile = open('%s_Lattice.dat' %mat, "w")
            if (TotalEnergy != 0 ):
                infile.write("%f\t%f \n" %(Lattice, TotalEnergy))
            infile.close()