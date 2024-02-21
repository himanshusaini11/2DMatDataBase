#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 20:40:50 2019

@author: enigma
"""

import numpy as np
from bokeh.plotting import figure, output_file, show

#infile = open('Bands.dat.gnu', 'r')
#header = infile.readline()
#header = header.split()
#FermiLevel = float(header[len(header)-2])

x = np.loadtxt('Bands.dat.gnu', dtype='float', comments='#', delimiter=None, 
               converters=None, skiprows=0, usecols=0, unpack=False, 
               ndmin=0, encoding='bytes')

#x = np.subtract(x, FermiLevel)
for i in range(0, 31):
    #z[0][i] = x[i]
    print (x[i])
#z = np.split(x, 62)

y = np.loadtxt('Bands.dat.gnu', dtype='float', comments='#', delimiter=None, 
               converters=None, skiprows=0, usecols=1, unpack=False, 
               ndmin=0, encoding='bytes')

output_file("Bands.html")
p = figure(width=700,height=350)
p.dash(x, y, size=500)
show(p)