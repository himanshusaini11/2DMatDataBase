#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 11:47:56 2019

@author: enigma
"""

def MatListData():
    MatName = []
    with open('MatList.dat', 'r') as infile:
        for l in infile.readlines():
            line = l.split()
            MatName.append(str(line[0]))
            
    infile.close()
    return MatName