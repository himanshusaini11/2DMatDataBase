#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 16:40:15 2019

@author: enigma
"""

import os

def Directory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' + directory)
        
def WriteInputFile(path, MatName, Postproc, filename, value):
    data_base = 'MaterialsDataBase/ElectronicProperties'
    Directory(path + '/' + data_base)
    dbpath = path + '/' + data_base
    
    Directory(dbpath + '/' + MatName)
    dbpath = dbpath + '/' + MatName + '/Analysis/' + Postproc
    Directory(dbpath)
    
    os.chdir(dbpath)
    infile = open(filename, 'w')
    infile.write(value)
    infile.close
    os.chdir(path)
    #completeName = os.path.join(path, '%s_%.2f.in' %(MatName, alat))
    #os.chdir(dbpath)
    #completeName = 'Bands.in'
    #infile = open(completeName, 'w')
    #infile.write(value)
    #infile.close()
    #os.chdir(path)

#def WriteInputFile(path, Property, MatName, filename, value):
#    DataBaseFolder = 'MaterialsDataBase'
#    Folder = 'ElectronicProperties'
#    writepath = path +'/%s/%s/%s/%s/' %(DataBaseFolder, Folder, MatName, Property)
#    os.chdir(writepath)
#    infile = open(filename, 'w')
#    infile.write(value)
#    infile.close
#    os.chdir(path)
    
def BandStructure():
    inputfile = str("""&bands
                 outdir = '../../Bands' ,
                filband = 'Bands.dat' ,
                 prefix = 'SCF-Bands' ,
                   lsym = .true. ,
 /""")
    return inputfile

def ChargeDensity():
    inputfile = str(""" &INPUTPP
                       prefix = 'SCF' ,
                      filplot = 'CD' ,
                     plot_num = 0 ,
                       outdir = '../../SCF' ,
 /

 &PLOT
                        nfile = 1 ,
                    filepp(1) = 'CD',
                    weight(1) = 1 ,
                        iflag = 3 ,
                output_format = 5 ,
                      fileout = 'CD.xsf' ,
 /""")
    return inputfile

def DensityOfStates():
    inputfile = str(""" &DOS
                      prefix = 'NSCF' ,
                      outdir = '../../NSCF' ,
                      fildos = 'DOS' ,
                      DeltaE = 0.001 ,
 /""")
    return inputfile

def ProjectedDensityOfStates():
    inputfile = str(""" &projwfc
                      outdir = '../../NSCF' ,
                      prefix = 'NSCF' ,
                      DeltaE = 0.001 ,
                     filpdos = 'PDOS' ,
/""")
    return inputfile

def WorkFunction():
    inputfile = str(""" &inputPP
                       prefix = 'SCF' ,
                       outdir = '../../SCF' ,
                     plot_num = 11 ,
                      filplot = 'WF.pot' ,
 /
 
 &plot
                        nfile = 1 ,
                    filepp(1) = 'WF.pot' ,
                    weight(1) = 1 
                        iflag = 3 ,
                output_format = 5 ,
                      fileout = 'WF.xsf' ,
 /""")
    return inputfile

def TotalPotential():
    inputfile = str("""  &inputPP
                   prefix = 'SCF' ,
                   outdir = '../../SCF' ,
                 plot_num = 1 ,
                  filplot = 'V_BHXC.pot' ,
 /
 
 &plot
                    nfile = 1 ,
                filepp(1) = 'V_BHXC.pot' ,
                weight(1) = 1 
                    iflag = 3 ,
            output_format = 5 ,
                  fileout = 'V_BHXC.xsf' ,
 /""")
    return inputfile

def Average(pot, npt):
    inputfile = str("""
1
%s.pot
1.D0
%i
3
12.3768849919""" %(pot, npt))
    return inputfile

def Npoints(path, mat):
    pathSCFOutFile = path + '/MaterialsDataBase/ElectronicProperties/' + mat + '/SCF/'
    SCFOutFile = 'SCF.out'
    
    os.chdir(pathSCFOutFile)
    infile = open(SCFOutFile, 'rt')
    for line in infile.readlines():
        if ('Dense  grid:' in line):
            npt = line.split()
            npt = npt[9]
            npt = int(npt[:-1])
            break
    os.chdir(path)
    
    return npt

def Analysis(path, MatName, PostProc):
    for j in range(0, len(PostProc)):
        filename = PostProc[j] + '.in'
        if (PostProc[j] == 'ChargeDensity'):
            inputdata = ChargeDensity()
            WriteInputFile(path, MatName, PostProc[j], filename, inputdata)
        elif (PostProc[j] == 'WorkFunction'):
            inputdata = WorkFunction()
            WriteInputFile(path, MatName, PostProc[j], filename, inputdata)
            npt = Npoints(path, MatName)
            pot = 'WF'
            inputdata = Average(pot, npt)
            filename = 'avg.in'
            WriteInputFile(path, MatName, PostProc[j], filename, inputdata)
        elif (PostProc[j] == 'TotalPotential'):
            inputdata = TotalPotential()
            WriteInputFile(path, MatName, PostProc[j], filename, inputdata)
            npt = Npoints(path, MatName)
            pot = 'V_BHXC'
            inputdata = Average(pot, npt)
            filename = 'avg.in'
            WriteInputFile(path, MatName, PostProc[j], filename, inputdata)
        elif (PostProc[j] == 'DensityOfStates'):
            inputdata = DensityOfStates()
            WriteInputFile(path, MatName, PostProc[j], filename, inputdata)
        elif (PostProc[j] == 'ProjectedDensityOfStates'):
            inputdata = ProjectedDensityOfStates()
            WriteInputFile(path, MatName, PostProc[j], filename, inputdata)
        else:
            inputdata = BandStructure()
            WriteInputFile(path, MatName, PostProc[j], filename, inputdata)
        #WriteInputFile(path, "Analysis/" + PostProc[j], MatName, filename, inputdata)
        #WriteInputFile(path, MatName, PostProc[j], filename, inputdata)