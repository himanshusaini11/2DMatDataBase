#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:50:48 2019

@author: enigma
"""

from src.Plotting.DOSPlotDAT import DOSPlot
from src.ReadMatList import MatListData
from bokeh.plotting import figure, output_file, show, save
from bokeh.io import export_png
import os
import numpy as np

MatName, alat = MatListData()
path = os.getcwd()
MatName1 = ['ClSSb']
for i in MatName1:
    pathDosDatFile = path + '/MaterialsDataBase/ElectronicProperties/' + i + '/Analysis/DensityOfStates/'
    pathSCFOutFile = path + '/MaterialsDataBase/ElectronicProperties/' + i + '/SCF/'
    
    SCFOutFile = 'SCF.out'

    os.chdir(pathSCFOutFile)
    infile = open(SCFOutFile, 'rt')
    for line in infile.readlines():
        if ('     the Fermi energy is' in line):
            FermiEnergy = line.split()
            FermiEnergy = float(FermiEnergy[4])
            break
    os.chdir(path)

    
    DosFile = 'DOS'
    os.chdir(pathDosDatFile)
    x, y, y_range = DOSPlot(DosFile, FermiEnergy)
    os.chdir(path)
    output_file("%s_DOS.html" %i)
    p = figure(width=600,height=350, x_range = (-3, 3), y_range = (0, np.max(y_range)),
               x_axis_label = 'Energy (eV)', y_axis_label = 'States', 
               title='Density of States')
    p.line((0, 0), (y.min(), y.max()), line_width = 1, line_color = "black", line_dash="4 4")
    p.line(x, y, line_width=2, line_color = "green")
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
    export_png(p, filename="%s_DOS.png" %i)
    save(p)
