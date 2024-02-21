#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:22:11 2019

@author: enigma
"""

import os
import subprocess

def RunAnalysisCalculation(path, mat, postproc, mpiproc):
    newpath = str(path + "/MaterialsDataBase/ElectronicProperties" + "/" + "%s/Analysis/%s" %(mat, postproc))
    os.chdir(newpath)
    inputfile = str("%s.in" %postproc)
    outputfile = str("%s.out" %postproc)
    #epPostProc = ['ChargeDensity', 'WorkFunction', 'TotalPotential', 'DensityOfStates', 'ProjectedDensityOfStates', 'BandStructure']
    if (postproc == 'ChargeDensity'):
        subprocess.call('mpiexec -n %i pp.x < %s |tee %s' %(mpiproc, inputfile, outputfile), shell = True)
    elif (postproc == 'WorkFunction' or postproc == 'TotalPotential'):
        subprocess.call('mpiexec -n %i pp.x < %s |tee %s' %(mpiproc, inputfile, outputfile), shell = True)
        subprocess.call('average.x < %s |tee %s' %('avg.in', 'avg.out'), shell = True)
    elif (postproc == 'DensityOfStates'):
        subprocess.call('mpiexec -n %i dos.x < %s |tee %s' %(mpiproc, inputfile, outputfile), shell = True)
    elif (postproc == 'ProjectedDensityOfStates'):
        subprocess.call('mpiexec -n %i projwfc.x < %s |tee %s' %(mpiproc, inputfile, outputfile), shell = True)
    elif (postproc == 'BandStructure'):
        subprocess.call('mpiexec -n %i bands.x < %s |tee %s' %(mpiproc, inputfile, outputfile), shell = True)
    #subprocess.call('mpiexec -n 4 pw.x < %s |tee %s' %(inputfile, outputfile), shell = True)
    os.chdir(path)