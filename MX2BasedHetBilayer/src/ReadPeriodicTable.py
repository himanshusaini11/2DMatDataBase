#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 20:38:13 2019

@author: enigma
"""

import pandas as pd
import numpy as np

def PeriodicTable():
    df = pd.read_excel('PeriodicTable.xls')
    arr = np.array(df)
    
    return arr
