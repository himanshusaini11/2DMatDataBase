#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:15:17 2019

@author: enigma
"""

import os
import subprocess

def CopyXML(path, DataBaseFolder, Folder, Property, MatName):
    copypath =  path +'/'+ DataBaseFolder +'/'+ Folder + '/' + MatName
    os.chdir(copypath)
    subprocess.call('cp -rf ./SCF/SCF.save ./NSCF/NSCF.save', shell = True)
    subprocess.call('cp -rf ./SCF/SCF.xml ./NSCF/NSCF.xml', shell = True)
    subprocess.call('cp -rf ./SCF/SCF.save ./Bands/SCF-Bands.save', shell = True)
    subprocess.call('cp -rf ./SCF/SCF.xml ./Bands/SCF-Bands.xml', shell = True)
    os.chdir(path)

def RunCalculation(program, inputfile, outputfile):
    subprocess.call('mpiexec -n 8 %s < %s |tee %s' %(program, inputfile, outputfile), shell = True)
    
def Run(path, DataBaseFolder, Folder, Property, MatName, PostProc):
    if (Folder == 'ElectronicProperties'):
        if (Property != 'Analysis'):
            calcpath = path +'/'+ DataBaseFolder +'/'+ Folder + '/' + MatName + '/' + Property
            os.chdir(calcpath)
            inputfile = str(Property + '.in')
            outputfile = str(Property + '.out')
            program = 'pw.x'
            RunCalculation(program, inputfile, outputfile)
            os.chdir(path)
        else:
            calcpath = path + '/' + DataBaseFolder+ '/' + Folder + '/' + MatName + '/' + Property + '/' + PostProc
            os.chdir(calcpath)
            inputfile = str(PostProc + '.in')
            outputfile = str(PostProc + '.out')
            
            if (PostProc == 'ChargeDensity' or PostProc == 'WorkFunction' or PostProc == 'TotalPotential'):
                program = 'pp.x'
                RunCalculation(program, inputfile, outputfile)
            elif (PostProc == 'DensityOfStates'):
                program = 'dos.x'
                RunCalculation(program, inputfile, outputfile)
            elif (PostProc == 'ProjectedDensityOfStates'):
                program = 'projwfc.x'
                RunCalculation(program, inputfile, outputfile)
            elif (PostProc == 'BandStructure'):
                program = 'bands.x'
                RunCalculation(program, inputfile, outputfile)
            os.chdir(path)
            
    elif (Folder == 'OpticalProperties'):
        if (Property != 'Analysis'):
            calcpath = path + '/' + DataBaseFolder + '/' + Folder + '/' + MatName + '/' + Property
            os.chdir(calcpath)
            inputfile = str(Property + '.in')
            outputfile = str(Property + '.out')
            program = 'pw.x'
            RunCalculation(program, inputfile, outputfile)
            os.chdir(path)
        else:
            calcpath = path + '/' + DataBaseFolder + '/' + Folder + '/' + MatName + '/' + Property + '/' + PostProc
            os.chdir(calcpath)
            inputfile = str(PostProc + '.in')
            outputfile = str(PostProc + '.out')
            
            if (PostProc == 'Epsilon'):
                program = 'epsilon.x'
                RunCalculation(program, inputfile, outputfile)
            os.chdir(path)