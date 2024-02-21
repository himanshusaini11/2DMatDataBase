#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:54:05 2019

@author: enigma
"""

from pbcpy.base import DirectCell, ReciprocalCell, Coord
import numpy as np

a = 3.1604
b = a
c = 20
#thickness = 3.172
#step = np.divide(thickness, 2)

A = np.array([np.divide(1, 2), -np.cos(np.radians(30)), 0])
B = np.array([np.divide(1, 2), np.cos(np.radians(30)), 0])
C = np.array([0, 0, 1])

CellA = np.multiply(A, a)
CellB = np.multiply(B, a)
CellC = np.multiply(C, c)

temp = [CellA, CellB, CellC]

lattice = np.ones(shape = (3,3))

for i in range(0, len(lattice)):
    lattice[i] = np.multiply(lattice[i], temp[i])


#lattice = np.identity(3)*10
cell1 = DirectCell(lattice = lattice, origin = [0, 0, 0])

print (cell1.lattice)
#print (cell1.volume)
reciprocal_cell1 = cell1.get_reciprocal()
#print (reciprocal_cell1.lattice)
cell2 = reciprocal_cell1.get_direct()
#print (cell2.lattice)
#print (cell1 == cell2)

pos1 = Coord(pos = [1.5802, -0.9123289, 8.414], cell = cell1)#, ctype = 'Cartesian')
#print (pos1.basis)
#print (type(pos1.cell))

#pos1 = Coord(pos=[0.5,0.0,1.0], cell=cell1, ctype="Crystal")
#pos2 = Coord(pos=[0.6,-1.0,3.0], cell=cell1, ctype="Crystal")

print (pos1.to_crys())