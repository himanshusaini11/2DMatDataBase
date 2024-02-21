#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:22:11 2019

@author: enigma
"""

import os
import subprocess

def RunEpsilon(path, mat, mpiprocs):
    newpath = str(path + "/MaterialsDataBase/OpticalProperties/%s" %mat)
    os.chdir(newpath)
    inputfile = str("IPA.in")
    outputfile = str("IPA.out")
    subprocess.call('mpiexec -n %i epsilon.x < %s |tee %s' %(mpiprocs, inputfile, outputfile), shell = True)
    os.chdir(path)
            
#path = os.getcwd()
#RunEOSCalculation(path)