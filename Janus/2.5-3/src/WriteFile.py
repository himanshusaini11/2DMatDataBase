#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 19:11:44 2019

@author: enigma
"""
import os

def WriteFile(path, filename, value):
    os.chdir(path)
    infile = open(filename, 'w')
    infile.write(value)
    infile.close