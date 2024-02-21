#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:29:09 2019

@author: enigma
"""

import sys
import os
import numpy as np
from PyQt5.QtWidgets import QDialog, QApplication, QScrollArea
from PyQt5.QtCore import pyqtSlot

from src.GUI.GUI_Get2dMaterialData import Ui_ScrollArea

#def Directory(directory):
#    try:
#        if not os.path.exists(directory):
#            os.makedirs(directory)
#    except OSError:
#        print ('Error: Creating directory. ' + directory)

class Get2DMat(QScrollArea):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ScrollArea()
        self.ui.setupUi(self)
        
        self.Data = {}
        
        self.ui.lineEdit_MaterialName.editingFinished.connect(self.MaterialName)
        self.ui.lineEdit_LatticeParameter.editingFinished.connect(self.LatticeParameter)
        self.ui.pushButton_AddData.clicked.connect(self.WriteData)
        self.ui.pushButton_Exit.clicked.connect(self.Exit)
        self.ui.pushButton_Overwrite.clicked.connect(self.Overwrite)
        
        self.show()
    
    def MaterialName(self):
        value = str(self.ui.lineEdit_MaterialName.text())
        return value
        
    def LatticeParameter(self):
        value = str(self.ui.lineEdit_LatticeParameter.text())
        return value
                
    def WriteData(self):
        self.ui.pushButton_Overwrite.setEnabled(False)
        MatName = str(self.MaterialName())
        Lattice = str(self.LatticeParameter())
        message = ""
        temp = False
        #infile = open('test.dat', 'a')
        #data = np.genfromtxt('test.dat', delimiter='\t')
        
        if (os.path.isfile('./MatList.dat') == True):
            if (len(self.Data) > 0):
                for i in self.Data:
                    if (i == MatName):
                        print (i)
                        message = str("Data already exist %s with Lattice %s . \nDo you want to overwrite then press overwrite. " %(i, self.Data[i]))
                        temp = True
                        self.ui.pushButton_Overwrite.setEnabled(True)
                        break
            if (temp != True):
                self.Data.update({MatName: Lattice})
            self.ui.label_Message.setText(message)
           
            #infile = open('MatList.dat', 'a')
            #for i in self.Data:
            #    infile.write("%s\t%s\n" %(i, self.Data[i]))
            
            #infile.close()
        else:
            if (len(self.Data) > 0):
                for i in self.Data:
                    if (i == MatName):
                        print (i)
                        message = str("Data already exist %s with Lattice %s . \nDo you want to overwrite then press overwrite. " %(i, self.Data[i]))
                        temp = True
                        self.ui.pushButton_Overwrite.setEnabled(True)
                        break
            if (temp != True):
                self.Data.update({MatName: Lattice})
            #print(self.Data)
            self.ui.label_Message.setText(message)
           
            #infile = open('MatList.dat', 'w')
            #for i in self.Data:
            #    infile.write("%s\t%s\n" %(i, self.Data[i]))
            
            #infile.close()
        infile = open('MatList.dat', 'w')
        for i in self.Data:
            infile.write("%s\t%s\n" %(i, self.Data[i]))
        infile.close()
        #self.close()
        
        
    def Exit(self):
        self.close()
        
        
    def Overwrite(self):
        MatName = str(self.MaterialName())
        Lattice = str(self.LatticeParameter())
        self.Data.update({MatName: Lattice})
        infile = open('MatList.dat', 'w')
        for i in self.Data:
            infile.write("%s \t %s \n" %(i, self.Data[i]))
        
        infile.close()
        self.ui.pushButton_Overwrite.setEnabled(False)
        self.ui.lineEdit_MaterialName.setText("")
        self.ui.lineEdit_LatticeParameter.setText("")
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Get2DMat()
    w.show()
    sys.exit(app.exec_())
