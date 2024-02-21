#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 10:29:38 2019

@author: enigma
"""

from src.ReadMatList import MatListData
from src.Plotting import BandPlotDAT
import os
from bokeh.plotting import figure, output_file, show, save
from bokeh.io import export_png
import numpy as np

MatName, alat = MatListData()
MatName1 = ['AsBrS', 'AsClS', 'AsClSe', 'AsClTe', 'ClSSb']
for mat in MatName1:
    path = os.getcwd()
    pathBandInFile = path + '/MaterialsDataBase/ElectronicProperties/' + mat + '/Bands/'
    pathBandsDatFile = path + '/MaterialsDataBase/ElectronicProperties/' + mat + '/Analysis/BandStructure/'
    pathSCFOutFile = path + '/MaterialsDataBase/ElectronicProperties/' + mat + '/SCF/'
    
    BandsInputFile = 'Bands.in'
    BandsDatFile = 'Bands.dat'
    BandStructureDOTOutFile = 'BandStructure.out'
    SCFOutFile = 'SCF.out'
    
    os.chdir(pathSCFOutFile)
    infile = open(SCFOutFile, 'rt')
    for line in infile.readlines():
        if ('     the Fermi energy is' in line):
            FermiEnergy = line.split()
            FermiEnergy = float(FermiEnergy[4])
            break
    os.chdir(path)
    
    os.chdir(pathBandsDatFile)
    nbnd, nks, eigenvalues = BandPlotDAT.GetEigenValues(BandsDatFile)
    os.chdir(path)
    
    eigenvalues = eigenvalues - FermiEnergy
    
    kpointpath = []
    kpointpathlable = [] 
    
    os.chdir(pathBandInFile)
    with open('Bands.in') as infile:
        copy = False
        for line in infile:
            if line.strip() == "K_POINTS {crystal_b}":
                copy = True
            elif line.strip() == " ":
                copy = False
            elif copy:
                kpointpath.append(line)
    os.chdir(path)
    
    no_HighSymmetryPoints = int(kpointpath[0])
    IntersectionPoints = int(kpointpath[1].split()[3])
    for i in range(1, len(kpointpath)):
        temp = kpointpath[i].split()
        if (temp != ''):
            kpointpathlable.append(temp[5])
            if (len(kpointpathlable) == no_HighSymmetryPoints):
                break
    
    os.chdir(pathBandsDatFile)
    kpointXCoordinates, kpoint = BandPlotDAT.GetKpointXCordinates(BandStructureDOTOutFile, 
                                                          IntersectionPoints, 
                                                          no_HighSymmetryPoints, 
                                                          nks)
    os.chdir(path)
    
    output_file('%s_BS.html' %mat)
    
    numlines = eigenvalues.shape[1]
    #mypalette=Spectral11[0:numlines]
    xmin = kpointXCoordinates[0]
    xmax = kpointXCoordinates[len(kpointXCoordinates)-1]
    ymin = eigenvalues.min()
    ymax = eigenvalues.max()
    
    p = figure(width=600, height=600, x_range = (xmin-0.1, xmax+0.1), y_range = (-3, 3),
               x_axis_label = 'K-Points', y_axis_label = 'Energy (eV)', 
               title='Band Structure') 
    for i in range(0, nbnd):
        p.line(kpointXCoordinates, eigenvalues[:, i], line_width = 2, line_color = "red")
        p.circle(kpointXCoordinates, eigenvalues[:, i], fill_color="white",line_color = "red", size=4)
        
        #p.multi_line(xs = kpointXCoordinates, ys = eigenvalues, line_width=5)
    p.xaxis.major_tick_line_color = None
    p.xaxis.minor_tick_line_color = None
    p.xaxis.major_label_text_font_size = '0pt'
    p.xaxis.major_label_text_font_size = '0pt' 
    p.yaxis.major_label_text_font_size = '15pt'
    #p.yaxis.major_lable_color = "orange"
    #p.yaxis.major_label_text_font_size = '10pt'
    p.yaxis.major_tick_line_width = 2
    p.yaxis.minor_tick_line_width = 2
    p.axis.major_tick_out = 10
    p.axis.minor_tick_out = 5
    p.xaxis.axis_label_text_font_size = "20pt"
    p.yaxis.axis_label_text_font_size = "20pt"
        
    p.line(kpointXCoordinates, 0, line_width = 1, line_color = "black", line_dash="4 4")
    for i in range(0, len(kpoint)):
        #print (i)
        x = kpoint.item(i)
        p.line((x, x), (ymin, ymax), line_width = 1, line_color = "black", line_dash="4 4")
    
    xdict = {}
    
    for i in range(0, len(kpoint)):
        if (i == 0):
            xdict[int(kpoint[i])] = str(kpointpathlable[i])
        else:
            xdict[float(kpoint[i])] = str(kpointpathlable[i])
    
    keys = np.fromiter(xdict.keys(), dtype=float)
    p.xaxis.ticker = keys
    p.xaxis.major_label_overrides = xdict
    p.xaxis.major_label_text_font_size = '15pt'
    p.xgrid.visible = False
    p.ygrid.visible = False
    p.outline_line_width = 2
    p.outline_line_alpha = 1
    p.outline_line_color = "black"
    
    export_png(p, filename="%s_BS.png" %mat)
    save(p)
