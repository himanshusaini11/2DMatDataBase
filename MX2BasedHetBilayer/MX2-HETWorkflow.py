#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 21:47:23 2019

@author: enigma
"""

import os
import numpy as np
from src import GetHeterostructureMX2Bilayer
from src import Bilayer_VC_Relax_InputFile, RunVCRelaxCalculations, ExtractInformationFromVCRelax
from src import SCF, RunSCFCalculations
from src import NSCF, RunNSCFCalculations
from src import Bands, RunBandsCalculations
from src import Analysis, RunAnalysisCalculations
from src import GetBandGap, GetPotential, GetCellParaAtomicPos, WriteMaterialInformation, LowdinAnalysis, GetTotalPotential
from src import Optical_SCF, RunOPT_SCFCalculations, OpticalAnalysis, RunOPT_Analysis
from src import Clean

mpiprocs = 28
VCRelaxDataBaseFolder = 'VCRelaxDataBase'
epPostProc = ['ChargeDensity', 'WorkFunction', 'TotalPotential', 'DensityOfStates', 'ProjectedDensityOfStates', 'BandStructure']

Bandgap = {}
Volume = {}
Density = {}
LatticeParameters = {}


infile = open('MatList.dat', 'r')
HetNames = infile.readlines()

calculationVCRelax = 'vc-relax'
calculationSCF = 'scf'
calculationNSCF = 'nscf'
calculationBands = 'bands'

pseudo_dir = '/opt/home/Himanshu/DataBaseProject/QE_Pseudo/PBE-PAW'
pseudo_dir_optical = '/opt/home/Himanshu/DataBaseProject/QE_Pseudo/NC'

prefix = 'Relax'
prefixSCF = 'SCF'
prefixNSCF = 'NSCF'
prefixBands = 'SCF-Bands'

ecutwfc = 60
ecutrho = 600
ecutwfc_opt = 150
ecutrho_opt = np.multiply(ecutwfc_opt, 4)
vdw_corr = 'DFT-D3'
nbnd = 80

infile = open('K_POINTS.pwscf', 'r')
K_POINTS = infile.read()
infile.close()

infile = open('MatList.dat', 'r')
HetNames = infile.readlines()

# epsilon.x inputfile parameteres
smeartype = 'lorentz'
intersmear = 0.136
intrasmear = 0.0
wmin = 0.05
wmax = 10
nbndmin = 1 
nbndmax = 80
nw = 3001
metalcalc = '.FALSE.'
shift = 0.0


path = os.getcwd()
for HetName in HetNames:
    HetName = HetName[:-1]
    Alat, AtomicCoordinates, CellParameters = GetHeterostructureMX2Bilayer.GetHeterostructureMX2Bilayer(path, HetName)
    Bilayer_VC_Relax_InputFile.AddFile(HetName, Alat, calculationVCRelax, pseudo_dir, prefix, ecutwfc, ecutrho, vdw_corr, AtomicCoordinates, CellParameters)
    RunVCRelaxCalculations.RunVCRelaxCalculation(path, HetName, mpiprocs)
    
    volume, density, AtomicCoordinates, CellParameters = ExtractInformationFromVCRelax.Information(path, VCRelaxDataBaseFolder, HetName)
    SCF.AddFile(HetName, Alat, calculationSCF, pseudo_dir, prefixSCF, ecutwfc, ecutrho, vdw_corr, AtomicCoordinates, CellParameters)
    RunSCFCalculations.RunSCFCalculation(path, HetName, mpiprocs)
    
    NSCF.AddFile(HetName, Alat, calculationNSCF, pseudo_dir, prefixNSCF, ecutwfc, ecutrho, vdw_corr, AtomicCoordinates, CellParameters)
    RunNSCFCalculations.RunNSCFCalculation(path, HetName, mpiprocs)
    
    Bands.AddFile(HetName, Alat, calculationBands, pseudo_dir, prefixBands, ecutwfc, ecutrho, vdw_corr, AtomicCoordinates, CellParameters)
    RunBandsCalculations.RunBandsCalculation(path, HetName, mpiprocs)
    
    Analysis.Analysis(path, HetName, epPostProc)
    for i in epPostProc:
        RunAnalysisCalculations.RunAnalysisCalculation(path, HetName, i, mpiprocs)
        
    alat = CellParameters[0].split()
    alat = np.multiply(np.multiply(float(alat[0]), Alat), 2)
    
    LatticeParameters[HetName] = alat, alat, float(CellParameters[2].split()[2])*Alat, 90, 90, 120
    Volume[HetName] = volume
    Density[HetName] = density
    
    Bandgap[HetName] = GetBandGap.BandGap(path, HetName)
    Potential = GetPotential.Potential(path, HetName)
    Potential[:, 1] = np.multiply(Potential[:, 1], 13.6056980659)
    Potential[:, 0] = np.multiply(Potential[:, 0], 0.529177249)
    VacuumLevel = Potential[:, 1].max()
    
    BandInfo = Bandgap[HetName]
    VBM_Vacc = BandInfo[1] - VacuumLevel
    CBM_Vacc = BandInfo[2] - VacuumLevel
    WorkFunction = VacuumLevel - BandInfo[3]
    
    cell_parameters, atomic_positions = GetCellParaAtomicPos.GetCellParaAtomicPos()
    AlatInfo = LatticeParameters[HetName]
    a = AlatInfo[0]
    b = AlatInfo[1]
    c = AlatInfo[2]
    alpha = AlatInfo[3]
    beta = AlatInfo[4]
    gamma = AlatInfo[5]
    unitcellVol = Volume[HetName]
    density = Density[HetName]
    bandgap = Bandgap[HetName]
    bandgap = bandgap[0]
    
    LowdinCharge = LowdinAnalysis.LowdinCharge(path, HetName)
    
    WriteMaterialInformation.WriteMatInfo(path, HetName, a, b, c, alpha, beta, gamma, unitcellVol, density, Alat, cell_parameters, atomic_positions, bandgap, VBM_Vacc, CBM_Vacc, WorkFunction, LowdinCharge)
    
    TotalPotential = GetTotalPotential.Potential(path, HetName)
    TotalPotential[:, 1] = np.multiply(TotalPotential[:, 1], 13.6056980659)
    TotalPotential[:, 0] = np.multiply(TotalPotential[:, 0], 0.529177249)
    TotalPotential[:, 1] -= TotalPotential[0, 1]
    InteristitialPotentialValue = TotalPotential[int(np.divide(len(TotalPotential), 2))][1]
    InteristitialPotential = {}
    InteristitialPotential[HetName] = InteristitialPotentialValue
    
    # Get Optical Properties.
    Optical_SCF.AddFile(HetName, Alat, calculationSCF, pseudo_dir_optical, prefixSCF, ecutwfc_opt, ecutrho_opt, vdw_corr, nbnd, AtomicCoordinates, CellParameters, K_POINTS)
    RunOPT_SCFCalculations.RunSCFCalculation(path, HetName, mpiprocs)
    OpticalAnalysis.IPA(path, HetName, smeartype, intersmear, intrasmear, wmin, wmax, nbndmin, nbndmax, nw, shift)
    RunOPT_Analysis.RunEpsilon(path, HetName, mpiprocs)
    
    Clean.CleanElectronicProperties(path, HetName)
    Clean.CleanOpticalProperties(path, HetName)
    Clean.CleanVCRelax(path, HetName)
    
outfile = open('InteristitialPot.dat', 'w')
for key, value in InteristitialPotential.items():
    outfile.write('%s\t%.6f\n' %(key, value))
    
outfile.close()
