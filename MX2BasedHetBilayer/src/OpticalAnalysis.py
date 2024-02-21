#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 13:47:07 2019

@author: enigma
"""

import os

def Directory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' + directory)
        
def WriteInputFile(path, MatName, filename, value):
    data_base = 'MaterialsDataBase/OpticalProperties'
    Directory(path + '/' + data_base)
    dbpath = path + '/' + data_base
    
    Directory(dbpath + '/' + MatName)
    dbpath = dbpath + '/' + MatName
    Directory(dbpath)
    
    os.chdir(dbpath)
    infile = open(filename, 'w')
    infile.write(value)
    infile.close
    os.chdir(path)
    
def IPA_Input(smeartype, intersmear, intrasmear, wmin, wmax, nbndmin, nbndmax, nw, shift):
    inputfile = str("""  &INPUTPP
   calculation = 'eps' ,
   prefix = 'SCF' ,
   outdir = './' ,
 /

 &ENERGY_GRID
   smeartype = '%s' ,
   intersmear = %.4f ,
   intrasmear = %.4f
   wmin = %.4f ,
   wmax = %.4f ,
   nbndmin = %i ,
   nbndmax = %i ,
   nw = %i ,
   shift = %.4f ,
 /""" %(smeartype, intersmear, intrasmear, wmin, wmax, nbndmin, nbndmax, nw, shift))
    return inputfile
    
def IPA(path, MatName, smeartype, intersmear, intrasmear, wmin, wmax, nbndmin, nbndmax, nw, shift):
    inputdata = IPA_Input(smeartype, intersmear, intrasmear, wmin, wmax, nbndmin, nbndmax, nw, shift)
    WriteInputFile(path, MatName, 'IPA.in', inputdata)