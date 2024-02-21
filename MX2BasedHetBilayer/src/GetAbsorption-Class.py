#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 19:31:20 2019

@author: enigma
"""

import numpy as np
import os

class OpticalProperties:
    def __init__(self, path, mat, polarization, system, deltaZ):
        self.path = path
        self.mat = mat
        self.polarization = polarization
        self.system = system
        self.deltaZ = deltaZ
        
        
    def DielectricFunction(self):
        readpath = path + '/MaterialsDataBase/OpticalProperties/' + self.mat
        os.chdir(readpath)
        real_part = np.loadtxt('epsr_SCF.dat', dtype = float, comments='#')
        imag_part = np.loadtxt('epsi_SCF.dat', dtype = float, comments='#')
                               
        return real_part, imag_part
    
    def ExtinctionCoefficient(self):
        real_part, imag_part = self.DielectricFunction()
        if (self.polarization == 'x' or self.polarization == 'X'):
            extinction = np.multiply((np.divide(1, np.sqrt(2))), (np.sqrt(np.add((-real_part[:, 1]), (np.sqrt(np.add((np.square(real_part[:, 1])), (np.square(imag_part[:, 1])))))))))
        elif (self.polarization == 'y' or self.polarization == 'Y'):
            extinction = np.multiply((np.divide(1, np.sqrt(2))), (np.sqrt(np.add((-real_part[:, 2]), (np.sqrt(np.add((np.square(real_part[:, 2])), (np.square(imag_part[:, 2])))))))))
        elif (self.polarization == 'z' or self.polarization == 'Z'):
            extinction = np.multiply((np.divide(1, np.sqrt(2))), (np.sqrt(np.add((-real_part[:, 3]), (np.sqrt(np.add((np.square(real_part[:, 3])), (np.square(imag_part[:, 3])))))))))
        
        return extinction
    
    def RefractiveIndex(self):
        real_part, imag_part = self.DielectricFunction()
        if (self.polarization == 'x' or self.polarization == 'X'):
            refractive_index = np.multiply((np.divide(1, np.sqrt(2))), (np.sqrt(np.add((real_part[:, 1]), (np.sqrt(np.add((np.square(real_part[:, 1])), (np.square(imag_part[:, 1])))))))))
        elif (self.polarization == 'y' or self.polarization == 'Y'):
            refractive_index = np.multiply((np.divide(1, np.sqrt(2))), (np.sqrt(np.add((real_part[:, 2]), (np.sqrt(np.add((np.square(real_part[:, 2])), (np.square(imag_part[:, 2])))))))))
        elif (self.polarization == 'z' or self.polarization == 'Z'):
            refractive_index = np.multiply((np.divide(1, np.sqrt(2))), (np.sqrt(np.add((real_part[:, 3]), (np.sqrt(np.add((np.square(real_part[:, 3])), (np.square(imag_part[:, 3])))))))))
        
        return refractive_index
    
    def Reflectivity(self):
        n = self.RefractiveIndex()
        k = self.ExtinctionCoefficient()
        reflectivity = np.divide((np.add((np.square(np.subtract((n), (1)))), (np.square(k)))), (np.add((np.square(np.add((n), (1)))), (np.square(k)))))
        
        return reflectivity
    
    def Absorption(self):
        real_part, imag_part = self.DielectricFunction()
        omega = np.divide((imag_part[:, 0]), (6.582119514E-16))
        
        if (self.system == '1D' or self.system == '2D'):
            if (self.polarization == 'x' or self.polarization == 'X'):
                Absorption = np.divide((np.multiply(imag_part[:, 1], omega)), (np.multiply(2.99792458E+8, 1))) # due to vacuum n = 1 in 2D and 1D case
            elif (self.polarization == 'y' or self.polarization == 'Y'):
                Absorption = np.divide((np.multiply(imag_part[:, 2], omega)), (np.multiply(2.99792458E+8, 1)))
            elif (self.polarization == 'z' or self.polarization == 'Z'):
                Absorption = np.divide((np.multiply(imag_part[:, 3], omega)), (np.multiply(2.99792458E+8, 1)))
                
        elif (self.system == '3D'):
            n = self.RefractiveIndex()
            if (self.polarization == 'x' or self.polarization == 'X'):
                Absorption = np.divide((np.multiply(imag_part[:, 1], omega)), (np.multiply(2.99792458E+8, n)))
            elif (self.polarization == 'y' or self.polarization == 'Y'):
                Absorption = np.divide((np.multiply(imag_part[:, 2], omega)), (np.multiply(2.99792458E+8, n)))
            elif (self.polarization == 'z' or self.polarization == 'Z'):
                Absorption = np.divide((np.multiply(imag_part[:, 3], omega)), (np.multiply(2.99792458E+8, n)))
        
        return Absorption
    
    def Absorbance(self):
        real_part, imag_part = self.DielectricFunction()
        omega = np.divide((imag_part[:, 0]), (6.582119514E-16))
        absorption = self.Absorption()
        if (self.polarization == 'x' or self.polarization == 'X'):
            Absorbance = np.subtract((1), (np.exp(-np.multiply((absorption), (self.deltaZ)))))
            #Absorbance = np.multiply((np.divide((np.multiply((omega), (imag_part[:, 1]))), (2.99792458E+8))), (deltaZ))
        elif (self.polarization == 'y' or self.polarization == 'Y'):
            Absorbance = np.multiply((np.divide((np.multiply((omega), (imag_part[:, 2]))), (2.99792458E+8))), (self.deltaZ))
        elif (self.polarization == 'z' or self.polarization == 'Z'):
            Absorbance = np.multiply((np.divide((np.multiply((omega), (imag_part[:, 2]))), (2.99792458E+8))), (self.deltaZ))
        
        return Absorbance

path = '/home/enigma/DataBaseProject/PythonScript/QE_MaterialsDataBase/IntersticialPotentialDB/Calculations/MX2-HET'
#Absorption = Absorption(path, 'MoS2-WSe2', 'x', '2D')
#Absorbance = Absorbance(path, 'MoS2-WSe2', 'x', '2D', 30E-10)
opt = OpticalProperties(path, 'MoS2-WSe2', 'x', '2D', 30E-10)
Absorbance = opt.Absorbance()
Absorption = opt.Absorption()
real_part, imag_part = opt.DielectricFunction()
photonEnergy = imag_part[:, 0]
    