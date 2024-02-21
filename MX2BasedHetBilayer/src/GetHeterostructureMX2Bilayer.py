#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 21:47:23 2019

@author: enigma
"""

from src.StructureDefinition.Hexagonal import Hexagonal
from src import ReadNumericalMatInfo

def GetHeterostructureMX2Bilayer(path, HetName):
    # Step 1: Collect Data for repective layers in Heterostructure.
    
    #path = os.getcwd()
    LayerInformation = {}
    #infile = open ('MatList.dat', 'r')
    #lines = infile.readlines()
    Layer = HetName.split('-')
    Layer[1] = Layer[1].split('\n')[0]
    
    for mat in Layer:
        LayerInformation[mat] = ReadNumericalMatInfo.ReadNumericalMatInfo(path, mat)
    
    Layer1 = LayerInformation[Layer[0]]
    Layer2 = LayerInformation[Layer[1]]
            
    # Step 2: Find the equivalent lattice parameter for Heterostructure.
    A_Het = (Layer1[2] + Layer2[2]) / 2
    
    # Step 3: Find the thickness (eg. S-S distance) in Layer1 and Layer2
    ThicknessL1 = Layer1[0][2, 2] - Layer1[0][1, 2]
    ThicknessL2 = Layer2[0][2, 2] - Layer2[0][1, 2]
    Thickness = [ThicknessL1, ThicknessL2]
    
    
    # Step 4: Find the Cell Parameters and Atomic Positions
    # Define StructureInformationMX2(LatticeParameter_a, Thickness, Vacuum, CompoundName, AtomicPositionUnit, LatticeCellUnit)
    #AtomicPositionUnit = 'angstrom'
    #LatticeCellUnit = 'angstrom'
    # Vacuum = C - (interlayer distance + Thickness1 + Thickness2)
    Vacuum = [30 - ThicknessL1, 30 - ThicknessL2]
    
    AtomicCoordinates = ['AtomicCoordinatesL1', 'AtomicCoordinatesL2']
    
    for i in range(0, len(Layer)):
        #AtomicCoordinates[i], CellParameters[i] = Hexagonal.StructureInformationMX2(A_Het, Thickness[i], Vacuum, Layer[i], AtomicPositionUnit, LatticeCellUnit)
        CellParameters, AtomicCoordinates[i] = Hexagonal.StructureMX2(A_Het, Thickness[i], Vacuum[i])
        
    # Step 5: Define interlayer distance and respective shifts in atomic coordinates.
    d = 3 # interlayer distance
    shift = [ThicknessL1/2 + d/2, ThicknessL2/2 + d/2]
    
    # Step 6: Find the respective Atomic Coordinates.
    AtomicCoordinates[0][:, 2] -= shift[0]
    AtomicCoordinates[1][:, 2] += shift[1]
    
    AtomicCoordinatesL1 = Hexagonal.AtomPositionsCrystal(CellParameters, AtomicCoordinates[0], Layer[0])
    AtomicCoordinatesL2 = Hexagonal.AtomPositionsCrystal(CellParameters, AtomicCoordinates[1], Layer[1])
    
    # Step 7: Append the Heterostructure Atomic Positions.
    AtomicPostionsHet = AtomicCoordinatesL2 + AtomicCoordinatesL1
    
    CellParameters = Hexagonal.CellParametersAlat(CellParameters, A_Het)
    
    return A_Het, AtomicPostionsHet, CellParameters