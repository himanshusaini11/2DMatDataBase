#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:09:20 2019

@author: enigma
"""

import numpy as np
from src.StructureDefinition.Hexagonal import CoordTransform

# Structure file for Hexagonal Lattice
def StructureInformationMX2(LatticeParameter_a, Thickness, Vacuum, CompoundName, AtomicPositionUnit, LatticeCellUnit):
    Cell, Atom = StructureMX2(LatticeParameter_a, Thickness, Vacuum)
    if (AtomicPositionUnit == 'Crystal' or AtomicPositionUnit == 'crystal'):
        AtomicCoordinates = AtomPositionsCrystal(Cell, Atom, CompoundName)
    elif (AtomicPositionUnit == 'Angstrom' or AtomicPositionUnit == 'Angstrom'):
        AtomicCoordinates = AtomPositionsCartesianAngstrom(Cell, Atom, CompoundName)
        
    if (LatticeCellUnit == 'Alat' or LatticeCellUnit == 'alat'):
        CellParameters = CellParametersAlat(Cell, LatticeParameter_a)
    elif (LatticeCellUnit == 'Angstrom' or LatticeCellUnit == 'Angstrom'):
        CellParameters = CellParametersAngstrom(Cell, LatticeParameter_a)
        
    return AtomicCoordinates, CellParameters
    

def StructureMX2(LatticeParameter_a, Thickness, Vacuum):
    a = LatticeParameter_a
    c = np.add(Thickness, Vacuum)
    step = np.divide(Thickness, 2)
    
    A = np.array([np.divide(1, 2), -np.cos(np.radians(30)), 0])
    B = np.array([np.divide(1, 2), np.cos(np.radians(30)), 0])
    C = np.array([0, 0, 1])
    
    CellA = np.multiply(A, a)
    CellB = np.multiply(B, a)
    CellC = np.multiply(C, c)
    
    Cell = np.array([CellA, CellB, CellC])
    
    Atom1 = np.array([np.divide(a, 2), np.multiply(np.divide(a, 3), np.cos(np.radians(30))), np.divide(c, 2)])
    Atom2 = np.array([np.divide(a, 2), -np.multiply(np.divide(a, 3), np.cos(np.radians(30))), np.subtract(np.divide(c, 2), step)])
    Atom3 = np.array([np.divide(a, 2), -np.multiply(np.divide(a, 3), np.cos(np.radians(30))), np.add(np.divide(c, 2), step)])
    
    Atom = np.array([Atom1, Atom2, Atom3])
    
    return Cell, Atom

def AtomPositionsCrystal(Cell, Atom, CompoundName):
    import re
    MX = ''.join([j for j in CompoundName if not j.isdigit()])
    elements = re.findall('[A-Z][^A-Z]*', MX)
    
    frac = CoordTransform.Fractional(Cell, Atom)
    temp = np.zeros(shape = (3,3))
    count = 0
    for j in frac:
        temp[count] = np.array(j)
        count += 1
    
    atom = {}
    count = 0
    elements = [elements[0], '%s1' %elements[1], '%s2' %elements[1]]
    
    float_formatter = lambda x: "%.12f" % x
    np.set_printoptions(formatter={'float_kind':float_formatter})
    
    for i in temp:
        var = elements[count]
        atom[var] = i
        count += 1
    
    information = []
    
    for i in atom:
        atomSymbol = ''.join([j for j in i if not j.isdigit()])
        var = str(atom[i]).lstrip('[').rstrip(']')
        
        information.append(str('%s\t%s'%(atomSymbol, var)))
    
    
    #file = open('AtomicPositions.dat', 'w')
    #for i in information:
    #    file.write('%s\n'%(str(i)))
    
    #file.close()
    return information
    
def AtomPositionsCartesianAngstrom(Cell, Atom, CompoundName):
    import re
    MX = ''.join([j for j in CompoundName if not j.isdigit()])
    elements = re.findall('[A-Z][^A-Z]*', MX)
    
    temp = np.zeros(shape = (3,3))
    count = 0
    for j in Atom:
        temp[count] = np.array(j)
        count += 1
    
    atom = {}
    count = 0
    elements = [elements[0], '%s1' %elements[1], '%s2' %elements[1]]
    
    float_formatter = lambda x: "%.12f" % x
    np.set_printoptions(formatter={'float_kind':float_formatter})
    
    for i in temp:
        var = elements[count]
        atom[var] = i
        count += 1
    
    information = []
    
    for i in atom:
        atomSymbol = ''.join([j for j in i if not j.isdigit()])
        var = str(atom[i]).lstrip('[').rstrip(']')
        
        information.append(str('%s\t%s'%(atomSymbol, var)))
    
    
    #file = open('AtomicPositions.dat', 'w')
    #for i in information:
    #    file.write('%s\n'%(str(i)))
    
    #file.close()
    return information
    
def CellParametersAlat(Cell, LatticeParameter_a):
    Cell = np.divide(Cell, LatticeParameter_a)
    information = []
    
    float_formatter = lambda x: "%.12f" % x
    np.set_printoptions(formatter={'float_kind':float_formatter})
    
    for i in Cell:
        #var = str(i.lstrip('[').rstrip(']'))
        var = str(i)
        
        information.append(str('%s'%(var[1:-1])))
    
    
    #file = open('Cell.dat', 'w')
    #for i in information:
    #    file.write('%s\n'%(str(i)))
    
    #file.close()
    return information
    
def CellParametersAngstrom(Cell, LatticeParameter_a):
    information = []
    float_formatter = lambda x: "%.12f" % x
    np.set_printoptions(formatter={'float_kind':float_formatter})
    
    for i in Cell:
        #var = str(i.lstrip('[').rstrip(']'))
        var = str(i)
        #print (var)
        
        information.append(str('%s'%(var[1:-1])))
    
    
    #file = open('Cell.dat', 'w')
    #for i in information:
    #    file.write('%s\n'%(str(i)))
    
    #file.close()
    return information
    

#a = 3.1604
#Thickness = 3.174
#Vacuum = 16.826
#CompoundName = 'MoS2'
#AtomicPositionUnit = 'Crystal'
#LatticeCellUnit = 'Alat'

#AtomicCoordinates, CellParameters = StructureInformationMX2(a, Thickness, Vacuum, CompoundName, AtomicPositionUnit, LatticeCellUnit)

#Cell, Atom = StructureMX2(a, Thickness, Vacuum)
#frac = CoordTransform.Fractional(Cell, Atom)


#AtomPositionsCrystal(a, Thickness, Vacuum, CompoundName)
#AtomPositionsCartesianAngstrom(a, Thickness, Vacuum, CompoundName)
