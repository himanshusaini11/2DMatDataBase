#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 20:00:17 2019

@author: enigma
"""

import sys
import os

def Directory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' + directory)
        
def MatDataBase(path, MatName):
    data_base = 'MaterialsDataBase/ElectronicProperties'
    calculations = ['SCF', 'NSCF', 'Bands', 'Analysis']
    analysis = ['NumericalResults', 'ChargeDensity', 'WorkFunction', 
                'TotalPotential', 'DensityOfStates', 
                'ProjectedDensityOfStates', 'BandStructure']
    len_calc = len(calculations)
    len_analysis = len(analysis)
    
    Directory(path + '/' + data_base)
    newpath = path + '/' + data_base
    
    if os.path.exists(newpath + '/' + MatName):
        sys.exit("Material Already Exist!!!!")
    else:
        #print ("The current working directory is %s" % path)
        Directory(newpath + '/' + MatName)
        newpath = newpath + '/' + MatName
    
    #print ("The current working directory is %s" % path)
    #Directory(path + '/' + MaterialName)
    #path = path + '/' + MaterialName
    
    #print ("The current working directory is %s" % path)
    for i in range (0, len_calc):
        Directory(newpath + '/' + calculations[i])
        temppath = ''
        #path = path + '/' + Calculations[i]
        #print ("The current working directory is %s" % path)
        temp = calculations[i]
        if (temp == 'Analysis'):
            temppath = newpath + '/' + temp
            for j in range (0, len_analysis):
                Directory(temppath + '/' + analysis[j])
        #if (temp == 'Relax'):
            #print (calculations[i])
            #temppath = newpath + '/' + calculations[i]
            #inputfile = str(calculations[i] + '.in')
            #outputfile = str(calculations[i] + '.out')
            #if (write == True):
            #WriteFile.WriteFile(temppath, inputfile, value)
            #RunCalculation.RunCalculation(inputfile, outputfile)
            #os.chdir(path)