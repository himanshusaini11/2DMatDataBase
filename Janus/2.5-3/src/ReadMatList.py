#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 18:43:17 2019

@author: enigma
"""

def MatListData():
    MatName = []
    alat = []
    with open('MatList.dat', 'r') as infile:
        for l in infile.readlines():
            line = l.split()
            MatName.append(str(line[0]))
            alat.append(str(line[1]))
            #MatName.append = str(line[0])
            #alat.append = str(line[1])
    infile.close()
    return MatName, alat