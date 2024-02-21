# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_GetOptInputFile.ui'
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
        self.label_Header.setGeometry(QtCore.QRect(20, 3, 1191, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Header.setFont(font)
        self.label_Header.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_Header.setObjectName("label_Header")
        self.plainTextEdit_InputText = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_InputText.setGeometry(QtCore.QRect(2, 160, 1221, 631))
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
"3. Make sure NCPP is used.\n"
"4. Use atleast 2 times or 3 times more nbnd.\n"
"5. Add the file."))
        self.plainTextEdit_InputText.setPlainText(_translate("ScrollArea_InputFileCreater", "\n"
" &CONTROL\n"
"                 calculation = \'scf\' ,\n"
"                      outdir = \'./\' ,\n"
"                  pseudo_dir = \'/opt/home/Himanshu/DataBaseProject/Janus/0-1/QE_Pseudo/NC\' ,\n"
"                      prefix = \'SCF\' ,\n"
"                   verbosity = \'high\' ,\n"
"                     tstress = .true. ,\n"
"                     tprnfor = .true. ,\n"
" /\n"
" &SYSTEM\n"
"%s\n"
"%s\n"
"%s\n"
"%s\n"
"                     ecutwfc = 150 ,\n"
"                 occupations = \'smearing\' ,\n"
"                     degauss = 3.6D-3 ,\n"
"                    smearing = \'fermi-dirac\' ,\n"
"                        nbnd = 80 ,\n"
"                       nosym = .true. ,\n"
" /\n"
" &ELECTRONS\n"
"            electron_maxstep = 150,\n"
"                    conv_thr = 1.0D-13 ,\n"
"                 mixing_mode = \'plain\' ,\n"
"                 mixing_beta = 0.3D0 ,\n"
"             diagonalization = \'david\' ,\n"
"              diago_full_acc = .true. ,\n"
" /\n"
"ATOMIC_SPECIES\n"
"  Cr 51.996100d0 Cr.UPF\n"
"  Se 78.960000d0 Se.UPF\n"
"  Te 127.600000d0 Te.UPF\n"
"%s    \n"
" K_POINTS crystal\n"
"          91\n"
"        0.0000000000    0.0000000000    0.0000000000    1.0\n"
"        0.0151515152    0.0000000000    0.0000000000    1.0\n"
"        0.0303030303    0.0000000000    0.0000000000    1.0\n"
"        0.0454545455    0.0000000000    0.0000000000    1.0\n"
"        0.0606060606    0.0000000000    0.0000000000    1.0\n"
"        0.0757575758    0.0000000000    0.0000000000    1.0\n"
"        0.0909090909    0.0000000000    0.0000000000    1.0\n"
"        0.1060606061    0.0000000000    0.0000000000    1.0\n"
"        0.1212121212    0.0000000000    0.0000000000    1.0\n"
"        0.1363636364    0.0000000000    0.0000000000    1.0\n"
"        0.1515151515    0.0000000000    0.0000000000    1.0\n"
"        0.1666666667    0.0000000000    0.0000000000    1.0\n"
"        0.1818181818    0.0000000000    0.0000000000    1.0\n"
"        0.1969696970    0.0000000000    0.0000000000    1.0\n"
"        0.2121212121    0.0000000000    0.0000000000    1.0\n"
"        0.2272727273    0.0000000000    0.0000000000    1.0\n"
"        0.2424242424    0.0000000000    0.0000000000    1.0\n"
"        0.2575757576    0.0000000000    0.0000000000    1.0\n"
"        0.2727272727    0.0000000000    0.0000000000    1.0\n"
"        0.2878787879    0.0000000000    0.0000000000    1.0\n"
"        0.3030303030    0.0000000000    0.0000000000    1.0\n"
"        0.3181818182    0.0000000000    0.0000000000    1.0\n"
"        0.3333333333    0.0000000000    0.0000000000    1.0\n"
"        0.3484848485    0.0000000000    0.0000000000    1.0\n"
"        0.3636363636    0.0000000000    0.0000000000    1.0\n"
"        0.3787878788    0.0000000000    0.0000000000    1.0\n"
"        0.3939393939    0.0000000000    0.0000000000    1.0\n"
"        0.4090909091    0.0000000000    0.0000000000    1.0\n"
"        0.4242424242    0.0000000000    0.0000000000    1.0\n"
"        0.4393939394    0.0000000000    0.0000000000    1.0\n"
"        0.4545454545    0.0000000000    0.0000000000    1.0\n"
"        0.4696969697    0.0000000000    0.0000000000    1.0\n"
"        0.4848484848    0.0000000000    0.0000000000    1.0\n"
"        0.5000000000    0.0000000000    0.0000000000    1.0\n"
"        0.4912278947    0.0175436842    0.0000000000    1.0\n"
"        0.4824557895    0.0350873684    0.0000000000    1.0\n"
"        0.4736836842    0.0526310526    0.0000000000    1.0\n"
"        0.4649115789    0.0701747368    0.0000000000    1.0\n"
"        0.4561394737    0.0877184211    0.0000000000    1.0\n"
"        0.4473673684    0.1052621053    0.0000000000    1.0\n"
"        0.4385952632    0.1228057895    0.0000000000    1.0\n"
"        0.4298231579    0.1403494737    0.0000000000    1.0\n"
"        0.4210510526    0.1578931579    0.0000000000    1.0\n"
"        0.4122789474    0.1754368421    0.0000000000    1.0\n"
"        0.4035068421    0.1929805263    0.0000000000    1.0\n"
"        0.3947347368    0.2105242105    0.0000000000    1.0\n"
"        0.3859626316    0.2280678947    0.0000000000    1.0\n"
"        0.3771905263    0.2456115789    0.0000000000    1.0\n"
"        0.3684184211    0.2631552632    0.0000000000    1.0\n"
"        0.3596463158    0.2806989474    0.0000000000    1.0\n"
"        0.3508742105    0.2982426316    0.0000000000    1.0\n"
"        0.3421021053    0.3157863158    0.0000000000    1.0\n"
"        0.3333300000    0.3333300000    0.0000000000    1.0\n"
"        0.3245581579    0.3245581579    0.0000000000    1.0\n"
"        0.3157863158    0.3157863158    0.0000000000    1.0\n"
"        0.3070144737    0.3070144737    0.0000000000    1.0\n"
"        0.2982426316    0.2982426316    0.0000000000    1.0\n"
"        0.2894707895    0.2894707895    0.0000000000    1.0\n"
"        0.2806989474    0.2806989474    0.0000000000    1.0\n"
"        0.2719271053    0.2719271053    0.0000000000    1.0\n"
"        0.2631552632    0.2631552632    0.0000000000    1.0\n"
"        0.2543834211    0.2543834211    0.0000000000    1.0\n"
"        0.2456115789    0.2456115789    0.0000000000    1.0\n"
"        0.2368397368    0.2368397368    0.0000000000    1.0\n"
"        0.2280678947    0.2280678947    0.0000000000    1.0\n"
"        0.2192960526    0.2192960526    0.0000000000    1.0\n"
"        0.2105242105    0.2105242105    0.0000000000    1.0\n"
"        0.2017523684    0.2017523684    0.0000000000    1.0\n"
"        0.1929805263    0.1929805263    0.0000000000    1.0\n"
"        0.1842086842    0.1842086842    0.0000000000    1.0\n"
"        0.1754368421    0.1754368421    0.0000000000    1.0\n"
"        0.1666650000    0.1666650000    0.0000000000    1.0\n"
"        0.1578931579    0.1578931579    0.0000000000    1.0\n"
"        0.1491213158    0.1491213158    0.0000000000    1.0\n"
"        0.1403494737    0.1403494737    0.0000000000    1.0\n"
"        0.1315776316    0.1315776316    0.0000000000    1.0\n"
"        0.1228057895    0.1228057895    0.0000000000    1.0\n"
"        0.1140339474    0.1140339474    0.0000000000    1.0\n"
"        0.1052621053    0.1052621053    0.0000000000    1.0\n"
"        0.0964902632    0.0964902632    0.0000000000    1.0\n"
"        0.0877184211    0.0877184211    0.0000000000    1.0\n"
"        0.0789465789    0.0789465789    0.0000000000    1.0\n"
"        0.0701747368    0.0701747368    0.0000000000    1.0\n"
"        0.0614028947    0.0614028947    0.0000000000    1.0\n"
"        0.0526310526    0.0526310526    0.0000000000    1.0\n"
"        0.0438592105    0.0438592105    0.0000000000    1.0\n"
"        0.0350873684    0.0350873684    0.0000000000    1.0\n"
"        0.0263155263    0.0263155263    0.0000000000    1.0\n"
"        0.0175436842    0.0175436842    0.0000000000    1.0\n"
"        0.0087718421    0.0087718421    0.0000000000    1.0\n"
"        0.0000000000    0.0000000000    0.0000000000    1.0"))
        self.pushButton_AddFile.setText(_translate("ScrollArea_InputFileCreater", "Add File"))
        self.pushButton_Exit.setText(_translate("ScrollArea_InputFileCreater", "Exit"))
        self.pushButton_Overwrite.setText(_translate("ScrollArea_InputFileCreater", "Overwrite"))
        self.label_MaterialInformation.setText(_translate("ScrollArea_InputFileCreater", "Material Name : Si\n"
"alat = 5.4306"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ScrollArea_InputFileCreater = QtWidgets.QScrollArea()
    ui = Ui_ScrollArea_InputFileCreater()
    ui.setupUi(ScrollArea_InputFileCreater)
    ScrollArea_InputFileCreater.show()
    sys.exit(app.exec_())

