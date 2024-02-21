#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 12:08:49 2019

@author: enigma
"""

import numpy as np
import os
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import gridplot
from src import ExtractOpticalProperties
"""
def ReadImaginaryDielectric(filename):
    value = np.loadtxt(filename, dtype='float', comments='#', delimiter=None, 
                   converters=None, skiprows=0, usecols=None, unpack=False, 
                   ndmin=0, encoding='bytes')
    
    return value

def ReadRealDielectric(filename):
    value = np.loadtxt(filename, dtype='float', comments='#', delimiter=None, 
                   converters=None, skiprows=0, usecols=None, unpack=False, 
                   ndmin=0, encoding='bytes')
    
    return value

def RefractiveIndex(epsilon_real, epsilon_imag):
    value = np.multiply(np.divide(1, np.sqrt(2)), np.sqrt(np.add(epsilon_real, np.sqrt(np.add(np.square(epsilon_real), np.square(epsilon_imag))))))
    return value

def ExtinctionCoefficient(epsilon_real, epsilon_imag):
    value = np.multiply(np.divide(1, np.sqrt(2)), np.sqrt(np.subtract(np.sqrt(np.add(np.square(epsilon_real), np.square(epsilon_imag))), epsilon_real)))
    return value

def Reflectivity(n, kappa):
    NUM = np.add(np.square(np.subtract(n, 1)), np.square(kappa))
    DEN = np.add(np.square(np.add(n, 1)), np.square(kappa))
    #value = np.divide((np.square(n - 1) + np.square(kappa)), (np.square(n + 1) + np.square(kappa)))
    value = np.divide(NUM, DEN, out = np.zeros_like(NUM), where = DEN != 0)
    return value

def AbsorptionCoefficient(PhotonEnergy_eV, PhotonWavelength_nm, epsilon_imag, refractiveIndex):
    h_cross = 6.582119514e-16
    c = 2.99792458e8
    omega_energy = np.divide(PhotonEnergy_eV, h_cross, out = np.zeros_like(PhotonEnergy_eV), where = PhotonEnergy_eV != 0)
    omega_wavelength = np.divide(PhotonWavelength_nm, h_cross, out = np.zeros_like(PhotonWavelength_nm), where = PhotonWavelength_nm != 0)
    NUM = np.multiply(epsilon_imag, omega_energy)
    DEN = np.multiply(c, refractiveIndex)
    alpha_energy = np.divide(NUM, DEN, out = np.zeros_like(NUM), where = DEN != 0)
    NUM = np.multiply(epsilon_imag, omega_wavelength)
    alpha_wavelength = np.divide(NUM, DEN, out = np.zeros_like(NUM), where = DEN != 0)
    
    return alpha_energy, alpha_wavelength, omega_energy, omega_wavelength
    
def Absorbance(alpha, thickness):
    absorbance = np.subtract(1, np.exp(-(np.multiply(alpha, np.multiply(thickness, 1e-10)))))
    absorbance_percent = np.multiply(absorbance, 100)
    
    return absorbance, absorbance_percent

def PlotOpticalProperties(x_data, y_data, xRange, xAxisLabel, yAxisLabel, Title):
    p = figure(width=600,height=350, x_range = xRange, y_range = (0, np.max(y_data)),
           x_axis_label = xAxisLabel, y_axis_label = yAxisLabel, 
           title = Title)
    p.line(x_data, y_data, line_width=2, line_color = "darkgreen")
    p.xaxis.axis_label_text_font_size = "15pt"
    p.yaxis.axis_label_text_font_size = "15pt"
    p.yaxis.major_label_text_font_size = '15pt'
    p.xaxis.major_label_text_font_size = '15pt'
    p.xgrid.visible = False
    p.ygrid.visible = False
    p.outline_line_width = 2
    p.outline_line_alpha = 1
    p.outline_line_color = "black"
    p.yaxis.major_tick_line_width = 2
    p.yaxis.minor_tick_line_width = 2
    p.xaxis.major_tick_line_width = 2
    p.xaxis.minor_tick_line_width = 2
    p.axis.major_tick_out = 10
    p.axis.minor_tick_out = 5
    
    return p
    
"""
path = os.getcwd()
DataBaseFolder = 'MaterialsDataBase'
Folder = 'OpticalProperties'
MatName = 'MoS2'
Property = 'Analysis/Epsilon'
ImagFileName = 'epsi_SCF.dat'
RealFileName = 'epsr_SCF.dat'
thickness = 20

readpath = path + '/%s/%s/%s/%s' %(DataBaseFolder, Folder, MatName, Property)

os.chdir(readpath)
ImagPart = ReadImaginaryDielectric(ImagFileName)
RealPart = ReadRealDielectric(RealFileName)
os.chdir(path)

PhotonEnergy_eV = np.array(ImagPart[:, 0], dtype = float, copy = True, order = 'C', subok = False)
PhotonWavelength_nm = np.divide(1.24, PhotonEnergy_eV, out = np.zeros_like(PhotonEnergy_eV), where = PhotonEnergy_eV != 0)
PhotonWavelength_nm = np.multiply(PhotonWavelength_nm, 1000)

ImagPart_X = np.array(ImagPart[:, 1], dtype = float, copy = True, order = 'C', subok = False)
ImagPart_Y = np.array(ImagPart[:, 2], dtype = float, copy = True, order = 'C', subok = False)
ImagPart_Z = np.array(ImagPart[:, 3], dtype = float, copy = True, order = 'C', subok = False)

RealPart_X = np.array(RealPart[:, 1], dtype = float, copy = True, order = 'C', subok = False)
RealPart_Y = np.array(RealPart[:, 2], dtype = float, copy = True, order = 'C', subok = False)
RealPart_Z = np.array(RealPart[:, 3], dtype = float, copy = True, order = 'C', subok = False)

refractiveIndex = RefractiveIndex(RealPart_X, ImagPart_X)
extinctionCoefficient = ExtinctionCoefficient(RealPart_X, ImagPart_X)
reflectivity = Reflectivity(refractiveIndex, extinctionCoefficient)

alpha_energy, alpha_wavelength, omega_energy, omega_wavelength = AbsorptionCoefficient(PhotonEnergy_eV, PhotonWavelength_nm, ImagPart_X, 1)
absorbance, absorbance_percent = Absorbance(alpha_energy, thickness)

alpha_energy = np.divide(alpha_energy, 100)
y_range = np.max(alpha_energy)

output_file("OPTTEST.html")

p = PlotOpticalProperties(PhotonEnergy_eV, alpha_energy, (0, 5), 'Energy (eV)', 'Absorption Coefficient (cm-1)', 'Absorption')
q = PlotOpticalProperties(PhotonEnergy_eV, absorbance_percent, (0, 5), 'Energy (eV)', 'Absorbance (%)', 'Absorbance')
r = PlotOpticalProperties(PhotonEnergy_eV, reflectivity, (0, 5), 'Energy (eV)', 'R(E)', 'Reflectivity')
s = PlotOpticalProperties(PhotonEnergy_eV, refractiveIndex, (0, 5), 'Energy (eV)', 'n(E)', 'Refractive Index')

grid = gridplot([p, q, r, s], ncols = 2, plot_width = 600, plot_height = 350)
show(grid)