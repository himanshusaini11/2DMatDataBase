#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:22:11 2019

@author: enigma
"""

import os
import subprocess

def RunVCRelaxCalculation(path, mat, mpiproc):
    newpath = str(path + "/VCRelaxDataBase" + "/" + "%s" %mat)
    os.chdir(newpath)
    inputfile = str("Relax.in")
    outputfile = str("Relax.out")
    subprocess.call('mpiexec -n %i pw.x < %s |tee %s' %(mpiproc, inputfile, outputfile), shell = True)
    os.chdir(path)
            
#path = os.getcwd()
#RunEOSCalculation(path)