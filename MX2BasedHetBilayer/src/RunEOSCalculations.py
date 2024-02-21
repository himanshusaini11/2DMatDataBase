#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:22:11 2019

@author: enigma
"""

import os
import subprocess
import numpy as np

def RunEOSCalculation(path, mat, alat_range):
    #lattice =float(startalat)
    newpath = str(path + "/EOSDataBase" + "/" + "%s" %mat)
    os.chdir(newpath)
    #alat_range = np.linspace(lattice - 1.5, lattice + 1.5, 20)
    for j in range(0, len(alat_range)):
        #path = str(path + "/" + "%s_%s.in" %(MatName[i], alat_range[j]))
        #pathin = str(path + "/" + "%s_%s.in" %(MatName[i], alat_range[j]))
        #pathout = str(path + "/" + "%s_%s.out" %(MatName[i], alat_range[j]))
        inputfile = str("%s_%.2f.in" %(mat, alat_range[j]))
        outputfile = str("%s_%.2f.out" %(mat, alat_range[j]))
        subprocess.call('mpiexec -n 4 pw.x < %s |tee %s' %(inputfile, outputfile), shell = True)
    os.chdir(path)
            
#path = os.getcwd()
#RunEOSCalculation(path)