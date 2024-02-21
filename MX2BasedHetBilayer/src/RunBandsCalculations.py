#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:22:11 2019

@author: enigma
"""

import os
import subprocess

def RunBandsCalculation(path, mat, mpiprocs):
    newpath = str(path + "/MaterialsDataBase/ElectronicProperties/%s/SCF" %mat)
    os.chdir(newpath)
    subprocess.call('cp -rf ./SCF.save ../Bands/SCF-Bands.save', shell = True)
    subprocess.call('cp -rf ./SCF.xml ../Bands/SCF-Bands.xml', shell = True)
    os.chdir(path)
    
    newpath = str(path + "/MaterialsDataBase/ElectronicProperties" + "/" + "%s/Bands" %mat)
    os.chdir(newpath)
    inputfile = str("Bands.in")
    outputfile = str("Bands.out")
    subprocess.call('mpiexec -n %i pw.x < %s |tee %s' %(mpiprocs, inputfile, outputfile), shell = True)
    os.chdir(path)
            
#path = os.getcwd()
#RunEOSCalculation(path)