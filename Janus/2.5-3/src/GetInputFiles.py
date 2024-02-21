#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:50:07 2019

@author: enigma
"""

import os

def WriteInputFile(path, DataBaseFolder, Folder, Property, MatName, filename, value):
    writepath = path +'/%s/%s/%s/%s/' %(DataBaseFolder, Folder, MatName, Property)
    os.chdir(writepath)
    infile = open(filename, 'w')
    infile.write(value)
    infile.close
    os.chdir(path)
    

def ExtractFinalCoordinates(path, DataBaseFolder, Folder, Property, MatName):
    readpath = path + '/%s/%s/%s/%s' %(DataBaseFolder,Folder, MatName, Property)
    with open(readpath + '/Relax.out') as infile, open(path + '/FinalCoordinate.dat', 'w') as outfile:
        copy = False
        for line in infile:
            if line.strip() == "Begin final coordinates":
                copy = True
            elif line.strip() == "End final coordinates":
                copy = False
            elif copy:
                outfile.write(line)
    infile.close()
    outfile.close()
                
def ExtractAtomicSpecies(path, DataBaseFolder, Folder, Property, MatName):
    readpath = path + '/%s/%s/%s/%s' %(DataBaseFolder,Folder, MatName, Property)
    with open(readpath + '/Relax.in') as infile, open(path + '/AtomicSpecies.dat', 'w') as outfile:
        copy = False
        for line in infile:
            if line.strip() == "ATOMIC_SPECIES":
                copy = True
            elif line.strip() == "ATOMIC_POSITIONS crystal":
                copy = False
            elif copy:
                outfile.write(line)
    infile.close()
    outfile.close()

def ExtractPseudoDir(path, DataBaseFolder, Folder, Property, MatName):
    readpath = path + '/%s/%s/%s/%s' %(DataBaseFolder,Folder, MatName, Property)
    with open(readpath + '/Relax.in') as infile, open(path + '/pseudo_dir.dat', 'w') as outfile:
        for line in infile:
            if ("pseudo_dir" in line):
                outfile.write(line)
    infile.close()
    outfile.close()
    
def ExtractIbrav(path, DataBaseFolder, Folder, Property, MatName):
    readpath = path + '/%s/%s/%s/%s' %(DataBaseFolder,Folder, MatName, Property)
    with open(readpath + '/Relax.in') as infile, open(path + '/ibrav.dat', 'w') as outfile:
        for line in infile:
            if ("ibrav" in line):
                outfile.write(line)
    infile.close()
    outfile.close()
                
def ExtractCelldm(path, DataBaseFolder, Folder, Property, MatName):
    readpath = path + '/%s/%s/%s/%s' %(DataBaseFolder,Folder, MatName, Property)
    with open(readpath + '/Relax.in') as infile, open(path + '/celldm.dat', 'w') as outfile:
        for line in infile:
            if ("celldm" in line):
                outfile.write(line)
    infile.close()
    outfile.close()
    
def ExtractNatom(path, DataBaseFolder, Folder, Property, MatName):
    readpath = path + '/%s/%s/%s/%s' %(DataBaseFolder,Folder, MatName, Property)
    with open(readpath + '/Relax.in') as infile, open(path + '/nat.dat', 'w') as outfile:
        for line in infile:
            if ("nat" in line):
                outfile.write(line)
    infile.close()
    outfile.close()
    
def ExtractNtype(path, DataBaseFolder, Folder, Property, MatName):
    readpath = path + '/%s/%s/%s/%s' %(DataBaseFolder,Folder, MatName, Property)
    with open(readpath + '/Relax.in') as infile, open(path + '/ntyp.dat', 'w') as outfile:
        for line in infile:
            if ("ntyp" in line):
                outfile.write(line)
    infile.close()
    outfile.close()

def SCF(calculation, PSEUDO_DIR, IBRAV, CELLDM, NAT, NTYP, ATOMIC_SPECIES, ATOMIC_POSITIONS):
    inputfile = str("""
                   
 &CONTROL
                 calculation = '%s' ,
                      outdir = './' ,
%s
                      prefix = 'SCF' ,
                   verbosity = 'high' ,
                     tstress = .true. ,
                     tprnfor = .true. ,
 /
 &SYSTEM
%s
%s
%s
%s
                     ecutwfc = 50 ,
                     ecutrho = 500 ,
                 occupations = 'smearing' ,
                     degauss = 3.6D-3 ,
                    smearing = 'fermi-dirac' ,
 /
 &ELECTRONS
            electron_maxstep = 150,
                    conv_thr = 1.0D-13 ,
                 mixing_mode = 'plain' ,
                 mixing_beta = 0.3D0 ,
             diagonalization = 'david' ,
              diago_full_acc = .true. ,
 /
 ATOMIC_SPECIES
%s

%s

K_POINTS automatic 
  24 24 1   0 0 0 

                   """ %(calculation, PSEUDO_DIR, IBRAV, CELLDM, NAT, NTYP, ATOMIC_SPECIES, ATOMIC_POSITIONS))
    return inputfile

def NSCF(calculation, PSEUDO_DIR, IBRAV, CELLDM, NAT, NTYP, ATOMIC_SPECIES, ATOMIC_POSITIONS):
    inputfile = str("""
                   
 &CONTROL
                 calculation = '%s' ,
                      outdir = './' ,
%s
                      prefix = 'NSCF' ,
                   verbosity = 'high' ,
                     tstress = .true. ,
                     tprnfor = .true. ,
 /
 &SYSTEM
%s
%s
%s
%s
                     ecutwfc = 50 ,
                     ecutrho = 500 ,
                 occupations = 'tetrahedra_opt' ,
 /
 &ELECTRONS
            electron_maxstep = 150,
                    conv_thr = 1.0D-9 ,
                 mixing_mode = 'plain' ,
                 mixing_beta = 0.3D0 ,
             diagonalization = 'david' ,
              diago_full_acc = .true. ,
 /
 ATOMIC_SPECIES
%s

%s

K_POINTS automatic 
  24 24 1   0 0 0 

                   """ %(calculation, PSEUDO_DIR, IBRAV, CELLDM, NAT, NTYP, ATOMIC_SPECIES, ATOMIC_POSITIONS))
    return inputfile

def BANDS(calculation, PSEUDO_DIR, IBRAV, CELLDM, NAT, NTYP, ATOMIC_SPECIES, ATOMIC_POSITIONS):
    inputfile = str("""
                   
 &CONTROL
                 calculation = '%s' ,
                      outdir = './' ,
%s
                      prefix = 'SCF-Bands' ,
                   verbosity = 'high' ,
                     tstress = .true. ,
                     tprnfor = .true. ,
 /
 &SYSTEM
%s
%s
%s
%s
                     ecutwfc = 50 ,
                     ecutrho = 500 ,
                 occupations = 'smearing' ,
                     degauss = 3.6D-3 ,
                    smearing = 'fermi-dirac' ,
 /
 &ELECTRONS
            electron_maxstep = 150,
                    conv_thr = 1.0D-9 ,
                 mixing_mode = 'plain' ,
                 mixing_beta = 0.3D0 ,
             diagonalization = 'david' ,
              diago_full_acc = .true. ,
 /
 ATOMIC_SPECIES
%s

%s

K_POINTS {crystal_b}
4 
   0.00 0.00 0.00 30 ! G
   0.00 0.50 0.00 30 ! M
   0.33 0.33 0.00 30 ! K
   0.00 0.00 0.00 30 ! G 

                   """ %(calculation, PSEUDO_DIR, IBRAV, CELLDM, NAT, NTYP, ATOMIC_SPECIES, ATOMIC_POSITIONS))
    return inputfile
                
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
                      DeltaE = 0.01 ,
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

def OpticalSCF(path, DataBaseFolder, Folder, Property, MatName, IBRAV, CELLDM, NAT, NTYP, ATOMIC_POSITIONS):
    readpath = path + '/%s/%s/%s/%s' %(DataBaseFolder, Folder, MatName, Property)
    os.chdir(readpath)
    inputfile = Property + '.in'
    infile = open(inputfile, 'rt')
    file = infile.read()
    #print (file)
    inputfile = str(file %(IBRAV, CELLDM, NAT, NTYP, ATOMIC_POSITIONS))
    infile.close()
    return inputfile

def Epsilon():
    inputfile = str(""" &INPUTPP
   calculation = 'eps' ,
   prefix = 'SCF' ,
   outdir = '../../OpticalSCF/' ,
 /

 &ENERGY_GRID
   smeartype = 'gaussian' ,
   intersmear = 0.1 ,
   wmin = 0.0 ,
   wmax = 100
   nw = 3001 ,
 /""")
    return inputfile
    

def GetInputFiles(path, DataBaseFolder, Folder, Property, MatName, PostProc):
    ExtractFinalCoordinates(path, DataBaseFolder, Folder, Property, MatName)
    ExtractAtomicSpecies(path, DataBaseFolder, Folder, Property, MatName)
    
    ExtractPseudoDir(path, DataBaseFolder, Folder, Property, MatName)
    ExtractIbrav(path, DataBaseFolder, Folder, Property, MatName)
    ExtractCelldm(path, DataBaseFolder, Folder, Property, MatName)
    ExtractNatom(path, DataBaseFolder, Folder, Property, MatName)
    ExtractNtype(path, DataBaseFolder, Folder, Property, MatName)
    
    infile1 = open('FinalCoordinate.dat', 'r')
    finalcoordinate = infile1.read()
    infile1.close()
    infile = open('AtomicSpecies.dat', 'r')
    atomicspecies = infile.read()
    infile.close
    infile = open('pseudo_dir.dat', 'r')
    pseudo_dir = infile.read()
    infile.close
    infile = open('ibrav.dat', 'r')
    ibrav = infile.read()
    infile.close
    infile = open('celldm.dat', 'r')
    celldm = infile.read()
    infile.close
    infile = open('nat.dat', 'r')
    nat = infile.read()
    infile.close
    infile = open('ntyp.dat', 'r')
    ntyp = infile.read()
    infile.close
        
    calculation = ['scf', 'nscf', 'bands']
    calculation_name = ['SCF', 'NSCF', 'Bands', 'Analysis', 'OpticalSCF']
    scfinput = SCF(calculation[0], pseudo_dir, ibrav, celldm, nat, ntyp, atomicspecies, finalcoordinate)
    nscfinput = NSCF(calculation[1], pseudo_dir, ibrav, celldm, nat, ntyp, atomicspecies, finalcoordinate)
    bandsinput = BANDS(calculation[2], pseudo_dir, ibrav, celldm, nat, ntyp, atomicspecies, finalcoordinate)
    if (Folder == 'ElectronicProperties'):
        for i in range(0, len(calculation_name)):
            filename = calculation_name[i] + '.in'
            if (calculation_name[i] == 'SCF'):
                WriteInputFile(path, DataBaseFolder, Folder, calculation_name[i], MatName, filename, scfinput)
            elif (calculation_name[i] == 'NSCF'):
                WriteInputFile(path, DataBaseFolder, Folder, calculation_name[i], MatName, filename, nscfinput)
            elif (calculation_name[i] == 'Bands'):
                WriteInputFile(path, DataBaseFolder, Folder, calculation_name[i], MatName, filename, bandsinput)
            elif (calculation_name[i] == 'Analysis'):
                for j in range(0, len(PostProc)):
                    filename = PostProc[j] + '.in'
                    if (PostProc[j] == 'ChargeDensity'):
                        inputdata = ChargeDensity()
                    elif (PostProc[j] == 'WorkFunction'):
                        inputdata = WorkFunction()
                    elif (PostProc[j] == 'TotalPotential'):
                        inputdata = TotalPotential()
                    elif (PostProc[j] == 'DensityOfStates'):
                        inputdata = DensityOfStates()
                    elif (PostProc[j] == 'ProjectedDensityOfStates'):
                        inputdata = ProjectedDensityOfStates()
                    else:
                        inputdata = BandStructure()
                    WriteInputFile(path, DataBaseFolder, Folder, calculation_name[i] + "/" + PostProc[j], MatName, filename, inputdata)

def GetOptInputFiles(path, DataBaseFolder, Folder, Property, MatName, PostProc):
    infile1 = open('FinalCoordinate.dat', 'r')
    finalcoordinate = infile1.read()
    infile1.close()
    infile = open('ibrav.dat', 'r')
    ibrav = infile.read()
    infile.close
    infile = open('celldm.dat', 'r')
    celldm = infile.read()
    infile.close
    infile = open('nat.dat', 'r')
    nat = infile.read()
    infile.close
    infile = open('ntyp.dat', 'r')
    ntyp = infile.read()
    infile.close
    
    calculation_name = ['OpticalSCF', 'Analysis']
    opticalscfinput = OpticalSCF(path, DataBaseFolder, Folder, Property, MatName, ibrav, celldm, nat, ntyp, finalcoordinate)
    
    if (Folder == 'OpticalProperties'):
        for i in range(0, len(calculation_name)):
            filename = calculation_name[i] + '.in'
            if (calculation_name[i] == 'OpticalSCF'):
                WriteInputFile(path, DataBaseFolder, Folder, calculation_name[i], MatName, filename, opticalscfinput)
            elif (calculation_name[i] == 'Analysis'):
                print ('OK')
                for j in range(0, len(PostProc)):
                    filename = PostProc[j] + '.in'
                    if (PostProc[j] == 'Epsilon'):
                        inputdata = Epsilon()
                    WriteInputFile(path, DataBaseFolder, Folder, calculation_name[i] + "/" + PostProc[j], MatName, filename, inputdata)
