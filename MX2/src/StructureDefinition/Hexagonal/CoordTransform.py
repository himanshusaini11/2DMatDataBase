#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 11:38:32 2019

@author: enigma
"""

import numpy as np

def Fractional(cellParam, cartCoords):
    cellParam = np.transpose(cellParam)
    fractionalCoordinates = []
    detCellParam = np.linalg.det(cellParam)
    for i in cartCoords:
        a = np.array([[i[0], cellParam[0][1], cellParam[0][2]], [i[1], cellParam[1][1], cellParam[1][2]], [i[2], cellParam[2][1], cellParam[2][2]]])
        b = np.array([[cellParam[0][0], i[0], cellParam[0][2]], [cellParam[1][0], i[1], cellParam[1][2]], [cellParam[2][0], i[2], cellParam[2][2]]])
        c = np.array([[cellParam[0][0], cellParam[0][1], i[0]], [cellParam[1][0], cellParam[1][1], i[1]], [cellParam[2][0], cellParam[2][1], i[2]]])
        
        a = np.divide(np.linalg.det(a), detCellParam)
        b = np.divide(np.linalg.det(b), detCellParam)
        c = np.divide(np.linalg.det(c), detCellParam)
        
        fractionalCoordinates.append([a, b, c])
        
    return fractionalCoordinates

def Cartesian(cellParam, fracCoords):
  cartesianCoordinates = []
  for i in fracCoords:
    x = i[0]*cellParam[0][0] + i[1]*cellParam[1][0] + i[2]*cellParam[2][0]
    y = i[0]*cellParam[0][1] + i[1]*cellParam[1][1] + i[2]*cellParam[2][1]
    z = i[0]*cellParam[0][2] + i[1]*cellParam[1][2] + i[2]*cellParam[2][2]
    
    cartesianCoordinates.append([x, y, z])
  return cartesianCoordinates
    