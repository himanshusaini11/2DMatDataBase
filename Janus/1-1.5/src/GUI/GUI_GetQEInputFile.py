# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_GetQEInputFile.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ScrollArea_InputFileCreater(object):
    def setupUi(self, ScrollArea_InputFileCreater):
        ScrollArea_InputFileCreater.setObjectName("ScrollArea_InputFileCreater")
        ScrollArea_InputFileCreater.resize(1228, 863)
        ScrollArea_InputFileCreater.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1226, 861))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_Header = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_Header.setGeometry(QtCore.QRect(20, 10, 1191, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Header.setFont(font)
        self.label_Header.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_Header.setObjectName("label_Header")
        self.plainTextEdit_InputText = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_InputText.setGeometry(QtCore.QRect(0, 160, 1221, 631))
        self.plainTextEdit_InputText.setOverwriteMode(True)
        self.plainTextEdit_InputText.setCursorWidth(5)
        self.plainTextEdit_InputText.setObjectName("plainTextEdit_InputText")
        self.pushButton_AddFile = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_AddFile.setGeometry(QtCore.QRect(930, 800, 80, 23))
        self.pushButton_AddFile.setObjectName("pushButton_AddFile")
        self.pushButton_Exit = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_Exit.setGeometry(QtCore.QRect(1030, 800, 80, 23))
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.pushButton_Overwrite = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_Overwrite.setEnabled(False)
        self.pushButton_Overwrite.setGeometry(QtCore.QRect(1130, 800, 80, 23))
        self.pushButton_Overwrite.setObjectName("pushButton_Overwrite")
        self.label_Message = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_Message.setEnabled(False)
        self.label_Message.setGeometry(QtCore.QRect(0, 800, 451, 61))
        self.label_Message.setText("")
        self.label_Message.setObjectName("label_Message")
        self.label_MaterialInformation = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_MaterialInformation.setGeometry(QtCore.QRect(20, 114, 231, 41))
        self.label_MaterialInformation.setObjectName("label_MaterialInformation")
        ScrollArea_InputFileCreater.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(ScrollArea_InputFileCreater)
        QtCore.QMetaObject.connectSlotsByName(ScrollArea_InputFileCreater)

    def retranslateUi(self, ScrollArea_InputFileCreater):
        _translate = QtCore.QCoreApplication.translate
        ScrollArea_InputFileCreater.setWindowTitle(_translate("ScrollArea_InputFileCreater", "Input File Creater"))
        self.label_Header.setText(_translate("ScrollArea_InputFileCreater", "Carefully read the instructions before you start:\n"
"1. Read the material name.\n"
"2. Please replace the sample text with given material name input file.\n"
"3. Replace calculation value with \'%s\', example (calculation = \'%s\' ,)\n"
"4. Add the file."))
        self.plainTextEdit_InputText.setPlainText(_translate("ScrollArea_InputFileCreater", "\n"
" &CONTROL\n"
"                 calculation = \'%s\' ,\n"
"                      outdir = \'./\' ,\n"
"                  pseudo_dir = \'/opt/home/Himanshu/DataBaseProject/Janus/0-1/QE_Pseudo/PBE-PAW\' ,\n"
"                      prefix = \'Relax\' ,\n"
"                   verbosity = \'low\' ,\n"
"                     disk_io = \'none\' ,\n"
"               etot_conv_thr = 1.0D-9 ,\n"
"               forc_conv_thr = 1.0D-6 ,\n"
"                       nstep = 100 ,\n"
"                     tstress = .true. ,\n"
"                     tprnfor = .true. ,\n"
" /\n"
" &SYSTEM\n"
"                       ibrav = 4,\n"
"                   celldm(1) = 6.3249133389 ,\n"
"                   celldm(3) = 5.9755004482 ,\n"
"                         nat = 3,\n"
"                        ntyp = 3,\n"
"                     ecutwfc = 50 ,\n"
"                     ecutrho = 500 ,\n"
"                 occupations = \'smearing\' ,\n"
"                     degauss = 3.6D-3 ,\n"
"                    smearing = \'fermi-dirac\' ,\n"
" /\n"
" &ELECTRONS\n"
"            electron_maxstep = 150,\n"
"                    conv_thr = 1.0D-13 ,\n"
"                 mixing_mode = \'plain\' ,\n"
"                 mixing_beta = 0.3D0 ,\n"
"             diagonalization = \'david\' ,\n"
"              diago_full_acc = .true. ,\n"
" /\n"
" &IONS\n"
" /\n"
"ATOMIC_SPECIES\n"
"  Cr 51.996100d0 Cr.UPF\n"
"  Se 78.960000d0 Se.UPF\n"
"  Te 127.600000d0 Te.UPF\n"
"ATOMIC_POSITIONS crystal \n"
"  Cr   0.3333535194d0   0.1667070393d0   0.5064453918d0\n"
"  Se   0.6666464806d0   0.8332929607d0   0.5819348658d0\n"
"  Te   0.6666464806d0   0.8332929607d0   0.4180651343d0\n"
"K_POINTS automatic \n"
"  24 24 1   0 0 0"))
        self.pushButton_AddFile.setText(_translate("ScrollArea_InputFileCreater", "Add File"))
        self.pushButton_Exit.setText(_translate("ScrollArea_InputFileCreater", "Exit"))
        self.pushButton_Overwrite.setText(_translate("ScrollArea_InputFileCreater", "Overwrite"))
        self.label_MaterialInformation.setText(_translate("ScrollArea_InputFileCreater", "Material Name : Silicon\n"
"alat = 5.4306"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ScrollArea_InputFileCreater = QtWidgets.QScrollArea()
    ui = Ui_ScrollArea_InputFileCreater()
    ui.setupUi(ScrollArea_InputFileCreater)
    ScrollArea_InputFileCreater.show()
    sys.exit(app.exec_())

