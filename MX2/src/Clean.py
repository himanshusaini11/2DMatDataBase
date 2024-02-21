#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 13:48:19 2019

@author: enigma
"""

import os
import subprocess

def CleanElectronicProperties(path, MatName):
    data_base = 'MaterialsDataBase/ElectronicProperties'
    dbpath = path + '/' + data_base + '/' + MatName
    
    os.chdir(dbpath)
    subprocess.call('rm -rf ./SCF/SCF.save', shell = True)
    subprocess.call('rm ./SCF/SCF.xml', shell = True)
    subprocess.call('rm -rf ./NSCF/NSCF.save', shell = True)
    subprocess.call('rm -rf ./NSCF/NSCF.xml', shell = True)
    subprocess.call('rm -rf ./Bands/SCF-Bands.save', shell = True)
    subprocess.call('rm -rf ./Bands/SCF-Bands.xml', shell = True)
    os.chdir(path)
    
def CleanOpticalProperties(path, MatName):
    data_base = 'MaterialsDataBase/OpticalProperties'
    dbpath = path + '/' + data_base + '/' + MatName
    
    os.chdir(dbpath)
    subprocess.call('rm -rf SCF.save', shell = True)
    subprocess.call('rm SCF.xml', shell = True)
    os.chdir(path)
    
def CleanVCRelax(path, MatName):
    data_base = 'VCRelaxDataBase'
    dbpath = path + '/' + data_base + '/' + MatName
    
    os.chdir(dbpath)
    subprocess.call('rm -rf Relax.save', shell = True)
    subprocess.call('rm Relax.xml', shell = True)
    os.chdir(path)