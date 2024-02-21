#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 20:00:17 2019

@author: enigma
"""

import sys
import os
import numpy as np
from src.Directory import Directory
from src import ReadMatList, WriteFile, RunCalculation

from PyQt5.QtWidgets import QDialog, QApplication, QScrollArea
from PyQt5.QtCore import pyqtSlot

from src.GUI.GUI_GetQEInputFile import Ui_ScrollArea_InputFileCreater

def MatDataBase(path, MatName, value):
    #print (path)
    #print (MatName)
    #print (write)
    #print (value)
    data_base = 'MaterialsDataBase/ElectronicProperties'
    calculations = ['Relax', 'SCF', 'NSCF', 'Bands', 'OpticalSCF', 'Analysis']
    analysis = ['NumericalResults', 'ChargeDensity', 'WorkFunction', 
                'TotalPotential', 'DensityOfStates', 
                'ProjectedDensityOfStates', 'BandStructure', 
                'Epsilon', 'Phonon']
    len_calc = len(calculations)
    len_analysis = len(analysis)
    
    Directory(path + '/' + data_base)
    newpath = path + '/' + data_base
    
    if os.path.exists(newpath + '/' + MatName):
        sys.exit("Material Already Exist!!!!")
    else:
        #print ("The current working directory is %s" % path)
        Directory(newpath + '/' + MatName)
        newpath = newpath + '/' + MatName
    
    #print ("The current working directory is %s" % path)
    #Directory(path + '/' + MaterialName)
    #path = path + '/' + MaterialName
    
    #print ("The current working directory is %s" % path)
    for i in range (0, len_calc):
        Directory(newpath + '/' + calculations[i])
        temppath = ''
        #path = path + '/' + Calculations[i]
        #print ("The current working directory is %s" % path)
        temp = calculations[i]
        if (temp == 'Analysis'):
            temppath = newpath + '/' + temp
            for j in range (0, len_analysis):
                Directory(temppath + '/' + analysis[j])
        if (temp == 'Relax'):
            #print (calculations[i])
            temppath = newpath + '/' + calculations[i]
            inputfile = str(calculations[i] + '.in')
            #outputfile = str(calculations[i] + '.out')
            #if (write == True):
            WriteFile.WriteFile(temppath, inputfile, value)
            #RunCalculation.RunCalculation(inputfile, outputfile)
            os.chdir(path)
                
class GetQEInputFile(QScrollArea):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ScrollArea_InputFileCreater()
        self.ui.setupUi(self)
        
        self.Data = {}
        self.counter = 0
        self.MatName, self.alat = ReadMatList.MatListData()
        #print (self.MatName)
        #print (self.alat)
        #self.alat = []
        
        self.ui.plainTextEdit_InputText.textChanged.connect(self.InputFile)
        self.ui.pushButton_AddFile.clicked.connect(self.CountAddClicked)
        self.ui.pushButton_Exit.clicked.connect(self.Exit)
        self.ui.pushButton_Overwrite.clicked.connect(self.Overwrite)
        
        self.show()
    
    def InputFile(self):
        value = str(self.ui.plainTextEdit_InputText.toPlainText())
        return value
    
    def CountAddClicked(self):
        self.AddFile(self.counter)
        self.counter +=1
        if (self.counter == len(self.MatName)):
            self.ui.pushButton_AddFile.setEnabled(False)
        else:
            self.ui.label_MaterialInformation.setText("Material Name : %s\nalat = %s" %(self.MatName[self.counter], self.alat[self.counter]))
        
      
    def AddFile(self, counter):
        self.ui.pushButton_Overwrite.setEnabled(False)
        path = os.getcwd()
        value = self.InputFile()
        temp = str('relax')
        inputdata = str(value %temp)
        MatDataBase(path, self.MatName[counter], inputdata)
 

    """
       temp = False
        if (temp == True):
            message = str("Input file %s_%.2f is already exist.\nDo you want to overwrite? Press Overwrite button." %(self.MatName[counter], self.alat[counter]))
            self.ui.label_Message.setEnabled(True)
            self.ui.label_Message.setText(message)
            self.ui.pushButton_Overwrite.setEnabled(True)
        else:
            value = self.InputFile()
            write = True
            temp = str('relax')
            #print (temp)
            #print (value)
            inputdata = str(value %temp)
            MatDataBase(path, self.MatName[counter], write, inputdata)
            #infile = open('%s_%.2f.in' %(MatName, alat), 'w')
            #infile.write(value)
            #infile.close()
            #return value
     """
       
    def Exit(self):
        self.close()
        
        
    def Overwrite(self):
        value = self.InputFile()
        MatName, alat = self.InputFileName()
        path = os.getcwd()
        write = True
        alat_range = np.linspace(alat - 1, alat + 1, 10)
        for i in range(0, len(alat_range)):
            temp = str(alat_range[i])
            inputdata = str(value %temp)
            MatDataBase(path, MatName, write, inputdata)
        #EOFDataBase(path, MatName, alat, write, value)
        #infile = open('%s_%.2f.in' %(MatName, alat), 'w')
        #infile.write(value)
        #infile.close()
        self.ui.pushButton_Overwrite.setEnabled(False)
        self.ui.label_Message.setText("")
        #return value
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = GetQEInputFile()
    w.show()
    sys.exit(app.exec_())