#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:22:11 2019

@author: enigma
"""

import os
import subprocess

def RunSCFCalculation(path, mat, mpiprocs):
    newpath = str(path + "/MaterialsDataBase/OpticalProperties/%s" %mat)
    os.chdir(newpath)
    inputfile = str("SCF.in")
    outputfile = str("SCF.out")
    subprocess.call('mpiexec -n %i pw.x < %s |tee %s' %(mpiprocs, inputfile, outputfile), shell = True)
    os.chdir(path)
            
#path = os.getcwd()
#RunEOSCalculation(path)