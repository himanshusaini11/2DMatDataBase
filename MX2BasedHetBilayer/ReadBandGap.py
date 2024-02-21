#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:04:21 2019

@author: Himanshu
"""

import os
from src import MatList
import numpy as np

MatName = MatList.MatListData()


path = os.getcwd()
readpath = str('%s/2DNumericalInformation' %path)
os.chdir(readpath)

bandgap = {}

for i in MatName:
    infile = open('%s_Info.dat' %i, 'r')
    data = infile.readlines()
    for line in data:
        if ('Band Gap' in line):
            temp = line.split()
            bandgap[i] = float(temp[3])
    infile.close()
    
Screen2D = {}
for i in bandgap:
    #print (bandgap[i])
    if (bandgap[i] >= 0.5):
        Screen2D[i] = bandgap[i]

MatArr = []
for i in Screen2D:
    MatArr.append(i)


outdata = []      
for i in range(0, len(MatArr)):
    #print (Screen2D[i])
    for j in range(0, len(MatArr)):
        if j != i & i > j:
            temp = MatArr[j]
            temp = MatArr[i] + "-" + temp
            outdata.append(temp)

os.chdir(path)            
outfile = open('MatListHet.dat', 'w')
for i in outdata:
    temp = i + "\n"
    outfile.write(temp)
outfile.close()