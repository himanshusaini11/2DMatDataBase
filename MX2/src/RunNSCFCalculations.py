#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:22:11 2019

@author: enigma
"""

import os
import subprocess

def RunNSCFCalculation(path, mat, mpiproc):
    newpath = str(path + "/MaterialsDataBase/ElectronicProperties/%s/SCF" %mat)
    os.chdir(newpath)
    subprocess.call('cp -rf ./SCF.save ../NSCF/NSCF.save', shell = True)
    subprocess.call('cp -rf ./SCF.xml ../NSCF/NSCF.xml', shell = True)
    os.chdir(path)
    
    newpath = str(path + "/MaterialsDataBase/ElectronicProperties" + "/" + "%s/NSCF" %mat)
    os.chdir(newpath)
    inputfile = str("NSCF.in")
    outputfile = str("NSCF.out")
    subprocess.call('mpiexec -n %i pw.x < %s |tee %s' %(mpiproc, inputfile, outputfile), shell = True)
    os.chdir(path)
            
#path = os.getcwd()
#RunEOSCalculation(path)