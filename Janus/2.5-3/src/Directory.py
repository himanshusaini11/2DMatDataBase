#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:02:47 2019

@author: enigma
"""

import os
import sys

def Directory(directory_name):
    try:
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
    except OSError:
        print ('Error: Creating directory. ' + directory_name)
        
def MaterialsDataBase(path, model_type, material_name):
    data_base = 'MaterialsDataBase'
    calculations = ['Relax', 'SCF', 'NSCF', 'Bands', 'OpticalSCF', 'Analysis']
    analysis = ['NumericalResults', 'ChargeDensity', 'WorkFunction', 
                'TotalPotential', 'DensityOfStates', 
                'ProjectedDensityOfStates', 'BandStructure', 
                'Epsilon', 'Phonon']
    len_calc = len(calculations)
    len_analysis = len(analysis)
    #print (lenCalc)
    #print (lenAnalysis)
    
    # detect the current working directory and print it
    #path = os.getcwd()
    #print ("The current working directory is %s" % path)
    
    Directory(path + '/' + data_base)
    path = path + '/' + data_base
    
    #print ("The current working directory is %s" % path)
    Directory(path + '/' + model_type)
    path = path + '/' + model_type
    
    if os.path.exists(path + '/' + material_name):
        sys.exit("Material Already Exist!!!!")
    else:
        #print ("The current working directory is %s" % path)
        Directory(path + '/' + material_name)
        path = path + '/' + material_name
    
    #print ("The current working directory is %s" % path)
    #Directory(path + '/' + MaterialName)
    #path = path + '/' + MaterialName
    
    #print ("The current working directory is %s" % path)
    for i in range (0, len_calc):
        Directory(path + '/' + calculations[i])
        #path = path + '/' + Calculations[i]
        #print ("The current working directory is %s" % path)
        temp = calculations[i]
        if (temp == 'Analysis'):
            path = path + '/' + temp
            for j in range (0, len_analysis):
                Directory(path + '/' + analysis[j])