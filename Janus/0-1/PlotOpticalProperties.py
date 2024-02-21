#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 12:08:49 2019

@author: enigma
"""

from src.ReadMatList import MatListData
import numpy as np
import os
from bokeh.plotting import output_file, show, save
from bokeh.io import export_png
from bokeh.layouts import gridplot
from src import ExtractOpticalProperties

path = os.getcwd()
MatName, alat = MatListData()
DataBaseFolder = 'MaterialsDataBase'
Folder = 'OpticalProperties'
Property = 'Analysis/Epsilon'
ImagFileName = 'epsi_SCF.dat'
RealFileName = 'epsr_SCF.dat'
thickness = 20

for mat in MatName:
    readpath = path + '/%s/%s/%s/%s' %(DataBaseFolder, Folder, mat, Property)
    
    os.chdir(readpath)
    ImagPart = ExtractOpticalProperties.ReadImaginaryDielectric(ImagFileName)
    RealPart = ExtractOpticalProperties.ReadRealDielectric(RealFileName)
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
    
    refractiveIndex = ExtractOpticalProperties.RefractiveIndex(RealPart_X, ImagPart_X)
    extinctionCoefficient = ExtractOpticalProperties.ExtinctionCoefficient(RealPart_X, ImagPart_X)
    reflectivity = ExtractOpticalProperties.Reflectivity(refractiveIndex, extinctionCoefficient)
    
    alpha_energy, alpha_wavelength, omega_energy, omega_wavelength = ExtractOpticalProperties.AbsorptionCoefficient(PhotonEnergy_eV, PhotonWavelength_nm, ImagPart_X, 1)
    absorbance, absorbance_percent = ExtractOpticalProperties.Absorbance(alpha_energy, thickness)
    
    alpha_energy = np.divide(alpha_energy, 100)
    y_range = np.max(alpha_energy)
    
    output_file("%s_OP.html" %mat)
    
    p = ExtractOpticalProperties.PlotOpticalProperties(PhotonEnergy_eV, alpha_energy, (0, 5), 'Energy (eV)', 'Absorption Coefficient (cm-1)', 'Absorption')
    q = ExtractOpticalProperties.PlotOpticalProperties(PhotonEnergy_eV, absorbance_percent, (0, 5), 'Energy (eV)', 'Absorbance (%)', 'Absorbance')
    r = ExtractOpticalProperties.PlotOpticalProperties(PhotonEnergy_eV, reflectivity, (0, 5), 'Energy (eV)', 'R(E)', 'Reflectivity')
    s = ExtractOpticalProperties.PlotOpticalProperties(PhotonEnergy_eV, refractiveIndex, (0, 5), 'Energy (eV)', 'n(E)', 'Refractive Index')
    
    grid = gridplot([p, q, r, s], ncols = 2, plot_width = 600, plot_height = 350)
    
    export_png(grid, filename="%s_DOS.png" %i)
    save(grid)
    #show(grid)
