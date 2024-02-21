#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 18:29:50 2019

@author: enigma
"""

import numpy as np

def DOSPlot(DosDatFile, FermiLevel):
    infile = open(DosDatFile, 'rt')
    header = infile.readline()
    header = header.split()
    #FermiLevel = float(header[len(header)-2])
    #print (FermiLevel)
    
    x = np.loadtxt(DosDatFile, dtype='float', comments='#', delimiter=None, 
                   converters=None, skiprows=0, usecols=0, unpack=False, 
                   ndmin=0, encoding='bytes')
    
    x = np.subtract(x, FermiLevel)
    
    y = np.loadtxt(DosDatFile, dtype='float', comments='#', delimiter=None, 
                   converters=None, skiprows=0, usecols=1, unpack=False, 
                   ndmin=0, encoding='bytes')
    
    for i in range(len(x)):
        if (x[i] < 5):
            maxindex = x[i]
        if (x[i] < -5):
            minindex = x[i]
    
    maxindex = x.tolist().index(maxindex)
    minindex = x.tolist().index(minindex)
    
    y_range = y[minindex:maxindex]
    
    return x, y, y_range