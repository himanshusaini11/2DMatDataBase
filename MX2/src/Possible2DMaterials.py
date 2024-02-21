#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 17:04:08 2019

@author: enigma
"""

import numpy as np
import pandas as pd

def TMDMaterials():
    file = "PeriodicTable.xls"
    df = pd.read_excel(file)
    
    #header = list(df)
    #print (df['Atomic Number'])
    ElementType = df[list(df)[4]].tolist()
    ElementName = df[list(df)[2]].tolist()
    
    TransitionMetals = []
    for i in range(0, len(ElementType)):
        temp = ElementType[i]
        #temp = ElementType[i]
        #print (temp)
        if (temp == "Transition Metal"):
            TransitionMetals.append(ElementName[i])
            
    Chalcogen = ['S', 'Se', 'Te']
    
    MX2 = []
    
    for i in TransitionMetals:
        for j in Chalcogen:
            temp = str("%s%s2" %(i, j))
            #print (temp)
            MX2.append(temp)
            
    infile = open('MatList.dat', 'w')
    for i in MX2:
        infile.write('%s\n' %i)
    
    infile.close()

"""
MXY = []

for i in TransitionMetals:
    for j in Chalcogen:
        for k in Chalcogen:
            if (k != j):
                temp = str("%s%s%s" %(i, j, k))
                MXY.append(temp)
        #temp = str("%s%s2" %(i, j))
        #print (temp)
        #MX2.append(temp)
        
infile = open('TotalMXY.dat', 'w')
for i in MXY:
    infile.write('%s\n' %i)

infile.close()
"""
