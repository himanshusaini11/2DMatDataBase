#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:56:14 2019

@author: enigma
"""

import os
import sys
from src import GetRelaxFile
from PyQt5.QtWidgets import QApplication

path = os.getcwd()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = GetRelaxFile.GetQEInputFile()
    w.show()
    sys.exit(app.exec_())
    
