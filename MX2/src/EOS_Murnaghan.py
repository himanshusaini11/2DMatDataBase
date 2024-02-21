#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 15:08:02 2019

@author: enigma
"""

import sys
import subprocess
import numpy as np
from scipy.optimize import leastsq

# Murnaghan equation of state
def EOS_Murnaghan(params, vol):
    'From Phys. Rev. B 28, 5480 (1983)'
    E0, B0, Bp, V0 = params 
    E = E0 + B0/Bp * vol * ((V0/vol)**Bp/(Bp-1.0)+1.0) - V0*B0/(Bp-1.0)
    return E

def EquivalentAlat(V0, c):
    A = np.sqrt(np.divide(V0, np.multiply(c, np.sin(np.deg2rad(60)))))
    return A

def print_params(label, params):
    E0, B0, Bp, V0 = params
    print (label, ": E0 = %f eV" % (E0))
    print (label, ": B0 = %f GPa" % (B0*160.21765))
    print (label, ": Bp = %f" % (Bp))
    print (label, ": V0 = %f angstrom^3" % (V0))
    
def MatListData():
    MatName = []
    alat = []
    with open('MatList.dat', 'r') as infile:
        for l in infile.readlines():
            line = l.split()
            MatName.append(str(line[0]))
            alat.append(str(line[1]))
            #MatName.append = str(line[0])
            #alat.append = str(line[1])
    infile.close()
    return MatName, alat

def VolumeTEData(path, MatName):
    subprocess.call('cp %s/EOSData/%s_Lattice.dat %s/volume.dat' %(path, MatName, path), shell = True)
    
def Main(path, MatName):
    VolumeTEData(path, MatName)
    #subprocess.call('cp %s/EOSData/%s_Lattice.dat %s/volume.dat' %(path, MatName, path), shell = True)
    #print ("OK")
    import os
    os.chdir(path)
    fname = 'volume.dat'
    if fname == '': fname = 'volume.dat'
    
    try:
        f = open(fname, 'rt')
    except IOError:
        sys.stderr.write("Error opening or reading file %s\n" % (fname))
        sys.exit(1)

    vol = []
    ene = []
    while True:
        line = f.readline().strip()
        if line == '': break
        if line[0] == '#' or line[0] == '!': continue
        v, e = [float(x) for x in line.split()[:2]]
        vol.append(v)
        ene.append(e)
    
    f.close()
    
    # transform to np arrays
    vol = np.array(vol)
    ene = np.array(ene)
    
    vol *= 0.14818471 
    ene *= 13.605692
    
    # fit a parabola to the data and get inital guess for equilibirum volume
    # and bulk modulus (least square polynomial fit)
    a, b, c = np.polyfit(vol, ene, 2)
    #print (a)
    #print (b)
    #print (c)
    V0 = -b/(2*a)
    E0 = a*V0**2 + b*V0 + c
    B0 = 2*a*V0
    Bp = 4.0
    
    # initial guesses in the same order used in the Murnaghan function
    x0 = [E0, B0, Bp, V0]
    
    
        
    
    # fit the equations of state
    target = lambda params, y, x: y - EOS_Murnaghan(params, x)
    murn, ier = leastsq(target, x0, args=(ene,vol))
    #print_params("Murnaghan", murn)
    A = EquivalentAlat(murn[3], 20)
    
    return A