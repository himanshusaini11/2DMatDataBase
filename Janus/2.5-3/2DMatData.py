#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:29:02 2019

@author: enigma
"""

#import ReadRelaxout
import os
import sys
from src import Get2dMaterialData
from PyQt5.QtWidgets import QApplication

path = os.getcwd()

#ReadRelaxout.GetInputFiles(path)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Get2dMaterialData.Get2DMat()
    w.show()
    sys.exit(app.exec_())
