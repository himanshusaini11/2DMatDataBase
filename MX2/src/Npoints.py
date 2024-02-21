#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 17:26:31 2019

@author: enigma
"""

import os
def Npoints(path, mat):
    pathSCFOutFile = path + '/MaterialsDataBase/ElectronicProperties/' + mat + '/SCF/'
    SCFOutFile = 'SCF.out'
    
    os.chdir(pathSCFOutFile)
    infile = open(SCFOutFile, 'rt')
    for line in infile.readlines():
        if ('Dense  grid:' in line):
            npt = line.split()
            npt = npt[9]
            npt = int(npt[:-1])
            break
    os.chdir(path)
    
    return npt