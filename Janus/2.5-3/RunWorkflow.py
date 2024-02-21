#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:54:13 2019

@author: enigma
"""

from src import RunCalculation
from src import GetInputFiles
from src import ReadMatList
import os

path = os.getcwd()
MatName, alat = ReadMatList.MatListData()

DataBaseFolder = 'MaterialsDataBase'
Folder = ['ElectronicProperties', 'OpticalProperties']
ElectronicProperty = ['Relax', 'SCF', 'NSCF', 'Bands', 'Analysis']
OpticalProperty = ['OpticalSCF', 'Analysis']
epPostPoc = ['ChargeDensity', 'WorkFunction', 'TotalPotential', 'DensityOfStates', 'ProjectedDensityOfStates', 'BandStructure']
opPostpoc = ['Epsilon']

for i in MatName:
    for j in Folder:
        if (j == 'ElectronicProperties'):
            for k in ElectronicProperty:
                l = 'nothing'
                if (k == 'Relax'):
                    RunCalculation.Run(path, DataBaseFolder, j, k, i, l)
                    GetInputFiles.GetInputFiles(path, DataBaseFolder, j, k, i, epPostPoc)
                elif (k == 'SCF'):
                    RunCalculation.Run(path, DataBaseFolder, j, k, i, l)
                    RunCalculation.CopyXML(path, DataBaseFolder, j, k, i)
                elif (k == 'Bands'):
                    RunCalculation.CopyXML(path, DataBaseFolder, j, k, i)
                    RunCalculation.Run(path, DataBaseFolder, j, k, i, l)
                elif (k == 'Analysis'):
                    for l in epPostPoc:
                        RunCalculation.CopyXML(path, DataBaseFolder, j, k, i)
                        RunCalculation.Run(path, DataBaseFolder, j, k, i, l)
                else:
                    RunCalculation.CopyXML(path, DataBaseFolder, j, k, i)
                    RunCalculation.Run(path, DataBaseFolder, j, k, i, l)
                    
        elif (j == 'OpticalProperties'):
            for k in OpticalProperty:
                l = 'nothing'
                if (k == 'OpticalSCF'):
                    RunCalculation.CopyXML(path, DataBaseFolder, j, k, i)
                    GetInputFiles.GetOptInputFiles(path, DataBaseFolder, j, k, i, opPostpoc)
                    RunCalculation.Run(path, DataBaseFolder, j, k, i, l)
                elif (k == 'Analysis'):
                    for l in opPostpoc:
                        RunCalculation.Run(path, DataBaseFolder, j, k, i, l)