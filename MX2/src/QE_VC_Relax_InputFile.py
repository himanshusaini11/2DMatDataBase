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
        
def VCRelaxDataBase(path, MatName, alat, value):
    data_base = 'VCRelaxDataBase'
    Directory(path + '/' + data_base)
    dbpath = path + '/' + data_base
    
    Directory(dbpath + '/' + MatName)
    dbpath = dbpath + '/' + MatName
    
    #completeName = os.path.join(path, '%s_%.2f.in' %(MatName, alat))
    os.chdir(dbpath)
    completeName = 'Relax.in'
    infile = open(completeName, 'w')
    infile.write(value)
    infile.close()
    os.chdir(path)

def InputFile(mat, calculation, pseudo_dir, prefix, celldm1, nat, ntyp, cell_parameters, atomic_species, atomic_positions):
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
               etot_conv_thr = 1.0D-7 ,
               forc_conv_thr = 1.0D-6 ,
                       nstep = 500 ,
                     tstress = .true. ,
                     tprnfor = .true. ,
 /
 &SYSTEM
                       ibrav = 0,
                   celldm(1) = %.10f,
                         nat = %i,
                        ntyp = %i,
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
  &IONS
                ion_dynamics = 'bfgs' ,
           pot_extrapolation = 'atomic' ,
           wfc_extrapolation = 'none' ,
            remove_rigid_rot = .false. ,
                     upscale = 100D0 ,
                   bfgs_ndim = 1 ,
            trust_radius_max = 0.8D0 ,
            trust_radius_min = 1D-3 ,
            trust_radius_ini = 0.5D0 ,
 /
 &CELL
               cell_dynamics = 'bfgs' ,
                       press = 0.0D0 ,
              press_conv_thr = 0.5D0 ,
                 cell_dofree = '2Dxy' ,
 /
CELL_PARAMETERS alat 
%s
ATOMIC_SPECIES
%s
ATOMIC_POSITIONS crystal 
%s
K_POINTS automatic 
  12 12 1   0 0 0 
""" %(mat, calculation, pseudo_dir, prefix, celldm1, nat, ntyp, cell_parameters, atomic_species, atomic_positions))
    return value


def AddFile(mat, a, Thickness, Vacuum, calculation, AtomicPositionUnit, LatticeCellUnit, pseudo_dir, prefix):
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
        
    ntyp = len(s)
    nat = len(elements)
                
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
    temp = np.divide(a, 0.529177249)
    inputdata = InputFile(mat, calculation, pseudo_dir, prefix, temp, nat, ntyp, cell_parameters, atomic_species, atomic_positions)
    #inputdata = str(value %temp)
    VCRelaxDataBase(path, mat, temp, inputdata)
            

#calculation = 'scf'
#pseudo_dir = '/home/enigma/'
#prefix = 'SCF'
#cell_parameters = str('011')
#atomic_species = str('011')
#atomic_positions = str('011')

#AddFile(calculation, pseudo_dir, prefix, cell_parameters, atomic_positions, atomic_species)