#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:50:48 2019

@author: enigma
"""

import numpy as np
from bokeh.plotting import figure, output_file, show

infile = open('DOS', 'r')
header = infile.readline()
header = header.split()
FermiLevel = float(header[len(header)-2])

x = np.loadtxt('DOS', dtype='float', comments='#', delimiter=None, 
               converters=None, skiprows=0, usecols=0, unpack=False, 
               ndmin=0, encoding='bytes')

x = np.subtract(x, FermiLevel)

y = np.loadtxt('DOS', dtype='float', comments='#', delimiter=None, 
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

output_file("DOS.html")
p = figure(width=700,height=350, x_range = (-5, 5), y_range = (0, np.max(y_range)),
           x_axis_label = 'Energy (eV)', y_axis_label = 'States ($eV^-1$)')
p.line(x, y, line_width=2)
show(p)
     