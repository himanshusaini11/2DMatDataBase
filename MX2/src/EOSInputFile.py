#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 21:47:23 2019

@author: enigma
"""

from src.StructureDefinition.Hexagonal import Hexagonal
from src import ReadPeriodicTable
import os
import numpy as np

def Directory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' + directory)
        
def EOFDataBase(path, MatName, alat, value):
    data_base = 'EOSDataBase'
    Directory(path + '/' + data_base)
    path = path + '/' + data_base
    
    Directory(path + '/' + MatName)
    path = path + '/' + MatName
    
    completeName = os.path.join(path, '%s_%.2f.in' %(MatName, alat))
    infile = open(completeName, 'w')
    infile.write(value)
    infile.close()

def MatListData():
    MatName = []
    with open('MatList.dat', 'r') as infile:
        for l in infile.readlines():
            line = l.split()
            MatName.append(str(line[0]))
            
    infile.close()
    return MatName
        
def InputFile(mat, calculation, pseudo_dir, prefix, celldm1, cell_parameters, atomic_species, atomic_positions):
    value = str("""
 &CONTROL
                       title = '%s-Monolayer' ,
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
                         nat = 3,
                        ntyp = 2,
                     ecutwfc = 60 ,
                     ecutrho = 600 ,
                       nosym = .false. ,
                   nosym_evc = .false. ,
                       noinv = .false. ,
                 occupations = 'smearing' ,
                     degauss = 3.6D-3 ,
                    smearing = 'fermi-dirac' ,
 /
 &ELECTRONS
            electron_maxstep = 100,
                    conv_thr = 1.0D-9 ,
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
K_POINTS automatic 
  12 12 1   0 0 0 
""" %(mat, calculation, pseudo_dir, prefix, celldm1, cell_parameters, atomic_species, atomic_positions))
    return value


def AddFile(mat, a, alat_range, Thickness, Vacuum, calculation, AtomicPositionUnit, LatticeCellUnit, pseudo_dir, prefix):
    #lattice =float(a)
    #alat_range = np.linspace(lattice -0.4, lattice + 1.5, 10)
    path = os.getcwd()
    CompoundName = mat
    AtomicCoordinates, CellParameters = Hexagonal.StructureInformationMX2(a, Thickness, Vacuum, CompoundName, AtomicPositionUnit, LatticeCellUnit)
    elements = {}
    count = 0
    for i in AtomicCoordinates:
        temp = i.split()
        elements[count] = np.array(temp[0])
        count +=1
        
    s = set()
    for dic in elements:
        s.add(str(elements[dic]))
        
    outfile = open('AtomicCoordinates.dat', 'w')
    for i in AtomicCoordinates:
        outfile.write('%s\n' %i)
    outfile.close()
    
    outfile = open('CellParameters.dat', 'w')
    for i in CellParameters:
        outfile.write('%s\n' %i)
    outfile.close()
    
    PeriodicTable = ReadPeriodicTable.PeriodicTable()
    AtomicSpecies = []
    for i in s:
        for j in PeriodicTable:
            #print ('%s\t%s' %(i, j[2]))
            temp = str(j[2])
            if (i == temp):
                temp = str('%s\t%s\t%s.UPF'%(temp, j[3], temp))
                AtomicSpecies.append(temp)
                
    outfile = open('AtomicSpecies.dat', 'w')
    for i in reversed(AtomicSpecies):
        outfile.write('%s\n' %i)
    outfile.close()
    
    infile = open('CellParameters.dat', 'rt')
    cell_parameters = infile.read()
    infile.close()
    infile = open('AtomicCoordinates.dat', 'rt')
    atomic_positions = infile.read()
    infile.close()
    infile = open('AtomicSpecies.dat', 'rt')
    atomic_species = infile.read()
    infile.close()
    for i in range(0, len(alat_range)):
        temp = float(alat_range[i]/0.52918)
        inputdata = InputFile(mat, calculation, pseudo_dir, prefix, temp, cell_parameters, atomic_species, atomic_positions)
        #inputdata = str(value %temp)
        EOFDataBase(path, mat, alat_range[i], inputdata)
            

#calculation = 'scf'
#pseudo_dir = '/home/enigma/'
#prefix = 'SCF'
#cell_parameters = str('011')
#atomic_species = str('011')
#atomic_positions = str('011')

#AddFile(calculation, pseudo_dir, prefix, cell_parameters, atomic_positions, atomic_species)