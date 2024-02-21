#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 21:47:23 2019

@author: enigma
"""

import os
import numpy as np

def Directory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' + directory)
        
def WriteInputFile(path, MatName, alat, value):
    data_base = 'MaterialsDataBase/OpticalProperties'
    Directory(path + '/' + data_base)
    dbpath = path + '/' + data_base
    
    Directory(dbpath + '/' + MatName)
    dbpath = dbpath + '/' + MatName
    Directory(dbpath)
    
    #completeName = os.path.join(path, '%s_%.2f.in' %(MatName, alat))
    os.chdir(dbpath)
    completeName = 'SCF.in'
    infile = open(completeName, 'w')
    infile.write(value)
    infile.close()
    os.chdir(path)

def InputFile(mat, calculation, pseudo_dir, prefix, celldm1, nat, ntyp, ecutwfc, ecutrho, vdw_corr, nbnd, cell_parameters, atomic_species, atomic_positions, K_POINTS):
    value = str("""
 &CONTROL
                       title = '%s-Heterostructure' ,
                 calculation = '%s' ,
                restart_mode = 'from_scratch' ,
                  wf_collect = .true. ,
                      outdir = '.' ,
                      wfcdir = '.' ,
                  pseudo_dir = '%s' ,
                      prefix = '%s' ,
                 lkpoint_dir = .true. ,
                   verbosity = 'high' ,
                     tstress = .true. ,
                     tprnfor = .true. ,
 /
 &SYSTEM
                       ibrav = 0,
                   celldm(1) = %.10f,
                         nat = %i,
                        ntyp = %i,
                     ecutwfc = %i ,
                     ecutrho = %i ,
                       nosym = .false. ,
                   nosym_evc = .false. ,
                       noinv = .false. ,
                 occupations = 'smearing' ,
                     degauss = 3.6D-3 ,
                    smearing = 'fermi-dirac' ,
                    vdw_corr = %s ,
                        nbnd = %i ,
 /
 &ELECTRONS
            electron_maxstep = 100,
                    conv_thr = 1.0D-13 ,
                 startingpot = 'atomic' ,
                 startingwfc = 'atomic+random' ,
                 mixing_mode = 'plain' ,
                 mixing_beta = 0.35D0 ,
                 mixing_ndim = 8,
             diagonalization = 'david' ,
              diago_thr_init = 1.0D-2 ,
              diago_full_acc = .true. ,
            diago_david_ndim = 8,
                         tqr = .false. ,
 /
CELL_PARAMETERS alat 
%s
ATOMIC_SPECIES
%s
ATOMIC_POSITIONS crystal 
%s
K_POINTS crystal 
%s
""" %(mat, calculation, pseudo_dir, prefix, celldm1, nat, ntyp, ecutwfc, ecutrho, vdw_corr, nbnd, cell_parameters, atomic_species, atomic_positions, K_POINTS))
    return value


def AddFile(mat, a, calulation, pseudo_dir, prefix, ecutwfc, ecutrho, vdw_corr, nbnd, AtomicCoordinates, CellParameters, K_POINTS):
    path = os.getcwd()
    elements = {}
    count = 0
    for i in AtomicCoordinates:
        temp = i.split()
        elements[count] = np.array(temp[0])
        count +=1
        
    s = set()
    for dic in elements:
        s.add(str(elements[dic]))
        
    ntyp = len(s)
    nat = len(elements)
                
    infile = open('CellParameters.dat', 'rt')
    cell_parameters = infile.read()
    infile.close()
    infile = open('AtomicCoordinates.dat', 'rt')
    atomic_positions = infile.read()
    infile.close()
    infile = open('AtomicSpecies.dat', 'rt')
    atomic_species = infile.read()
    infile.close()
    celldm1 = np.divide(a, 0.529177249)
    inputdata = InputFile(mat, calulation, pseudo_dir, prefix, celldm1, nat, ntyp, ecutwfc, ecutrho, vdw_corr, nbnd, cell_parameters, atomic_species, atomic_positions, K_POINTS)
    #inputdata = str(value %temp)
    WriteInputFile(path, mat, temp, inputdata)