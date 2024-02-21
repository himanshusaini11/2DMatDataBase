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
"                  pseudo_dir = \'/home/enigma/DataBaseProject/PythonScript/QE_MaterialsDataBase/IntersticialPotentialDB/Calculations/Si-Based/QE_Pseudo/NC\' ,\n"
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
"  Si 28.085500d0 Si.UPF\n"
"%s    \n"
" K_POINTS crystal\n"
"         151\n"
"        0.5000000000    0.7500000000    0.2500000000    1.0\n"
"        0.4875000000    0.7312500000    0.2437500000    1.0\n"
"        0.4750000000    0.7125000000    0.2375000000    1.0\n"
"        0.4625000000    0.6937500000    0.2312500000    1.0\n"
"        0.4500000000    0.6750000000    0.2250000000    1.0\n"
"        0.4375000000    0.6562500000    0.2187500000    1.0\n"
"        0.4250000000    0.6375000000    0.2125000000    1.0\n"
"        0.4125000000    0.6187500000    0.2062500000    1.0\n"
"        0.4000000000    0.6000000000    0.2000000000    1.0\n"
"        0.3875000000    0.5812500000    0.1937500000    1.0\n"
"        0.3750000000    0.5625000000    0.1875000000    1.0\n"
"        0.3625000000    0.5437500000    0.1812500000    1.0\n"
"        0.3500000000    0.5250000000    0.1750000000    1.0\n"
"        0.3375000000    0.5062500000    0.1687500000    1.0\n"
"        0.3250000000    0.4875000000    0.1625000000    1.0\n"
"        0.3125000000    0.4687500000    0.1562500000    1.0\n"
"        0.3000000000    0.4500000000    0.1500000000    1.0\n"
"        0.2875000000    0.4312500000    0.1437500000    1.0\n"
"        0.2750000000    0.4125000000    0.1375000000    1.0\n"
"        0.2625000000    0.3937500000    0.1312500000    1.0\n"
"        0.2500000000    0.3750000000    0.1250000000    1.0\n"
"        0.2375000000    0.3562500000    0.1187500000    1.0\n"
"        0.2250000000    0.3375000000    0.1125000000    1.0\n"
"        0.2125000000    0.3187500000    0.1062500000    1.0\n"
"        0.2000000000    0.3000000000    0.1000000000    1.0\n"
"        0.1875000000    0.2812500000    0.0937500000    1.0\n"
"        0.1750000000    0.2625000000    0.0875000000    1.0\n"
"        0.1625000000    0.2437500000    0.0812500000    1.0\n"
"        0.1500000000    0.2250000000    0.0750000000    1.0\n"
"        0.1375000000    0.2062500000    0.0687500000    1.0\n"
"        0.1250000000    0.1875000000    0.0625000000    1.0\n"
"        0.1125000000    0.1687500000    0.0562500000    1.0\n"
"        0.1000000000    0.1500000000    0.0500000000    1.0\n"
"        0.0875000000    0.1312500000    0.0437500000    1.0\n"
"        0.0750000000    0.1125000000    0.0375000000    1.0\n"
"        0.0625000000    0.0937500000    0.0312500000    1.0\n"
"        0.0500000000    0.0750000000    0.0250000000    1.0\n"
"        0.0375000000    0.0562500000    0.0187500000    1.0\n"
"        0.0250000000    0.0375000000    0.0125000000    1.0\n"
"        0.0125000000    0.0187500000    0.0062500000    1.0\n"
"        0.0000000000    0.0000000000    0.0000000000    1.0\n"
"        0.0138888889    0.0138888889    0.0000000000    1.0\n"
"        0.0277777778    0.0277777778    0.0000000000    1.0\n"
"        0.0416666667    0.0416666667    0.0000000000    1.0\n"
"        0.0555555556    0.0555555556    0.0000000000    1.0\n"
"        0.0694444444    0.0694444444    0.0000000000    1.0\n"
"        0.0833333333    0.0833333333    0.0000000000    1.0\n"
"        0.0972222222    0.0972222222    0.0000000000    1.0\n"
"        0.1111111111    0.1111111111    0.0000000000    1.0\n"
"        0.1250000000    0.1250000000    0.0000000000    1.0\n"
"        0.1388888889    0.1388888889    0.0000000000    1.0\n"
"        0.1527777778    0.1527777778    0.0000000000    1.0\n"
"        0.1666666667    0.1666666667    0.0000000000    1.0\n"
"        0.1805555556    0.1805555556    0.0000000000    1.0\n"
"        0.1944444444    0.1944444444    0.0000000000    1.0\n"
"        0.2083333333    0.2083333333    0.0000000000    1.0\n"
"        0.2222222222    0.2222222222    0.0000000000    1.0\n"
"        0.2361111111    0.2361111111    0.0000000000    1.0\n"
"        0.2500000000    0.2500000000    0.0000000000    1.0\n"
"        0.2638888889    0.2638888889    0.0000000000    1.0\n"
"        0.2777777778    0.2777777778    0.0000000000    1.0\n"
"        0.2916666667    0.2916666667    0.0000000000    1.0\n"
"        0.3055555556    0.3055555556    0.0000000000    1.0\n"
"        0.3194444444    0.3194444444    0.0000000000    1.0\n"
"        0.3333333333    0.3333333333    0.0000000000    1.0\n"
"        0.3472222222    0.3472222222    0.0000000000    1.0\n"
"        0.3611111111    0.3611111111    0.0000000000    1.0\n"
"        0.3750000000    0.3750000000    0.0000000000    1.0\n"
"        0.3888888889    0.3888888889    0.0000000000    1.0\n"
"        0.4027777778    0.4027777778    0.0000000000    1.0\n"
"        0.4166666667    0.4166666667    0.0000000000    1.0\n"
"        0.4305555556    0.4305555556    0.0000000000    1.0\n"
"        0.4444444444    0.4444444444    0.0000000000    1.0\n"
"        0.4583333333    0.4583333333    0.0000000000    1.0\n"
"        0.4722222222    0.4722222222    0.0000000000    1.0\n"
"        0.4861111111    0.4861111111    0.0000000000    1.0\n"
"        0.5000000000    0.5000000000    0.0000000000    1.0\n"
"        0.5000000000    0.5138888889    0.0138888889    1.0\n"
"        0.5000000000    0.5277777778    0.0277777778    1.0\n"
"        0.5000000000    0.5416666667    0.0416666667    1.0\n"
"        0.5000000000    0.5555555556    0.0555555556    1.0\n"
"        0.5000000000    0.5694444444    0.0694444444    1.0\n"
"        0.5000000000    0.5833333333    0.0833333333    1.0\n"
"        0.5000000000    0.5972222222    0.0972222222    1.0\n"
"        0.5000000000    0.6111111111    0.1111111111    1.0\n"
"        0.5000000000    0.6250000000    0.1250000000    1.0\n"
"        0.5000000000    0.6388888889    0.1388888889    1.0\n"
"        0.5000000000    0.6527777778    0.1527777778    1.0\n"
"        0.5000000000    0.6666666667    0.1666666667    1.0\n"
"        0.5000000000    0.6805555556    0.1805555556    1.0\n"
"        0.5000000000    0.6944444444    0.1944444444    1.0\n"
"        0.5000000000    0.7083333333    0.2083333333    1.0\n"
"        0.5000000000    0.7222222222    0.2222222222    1.0\n"
"        0.5000000000    0.7361111111    0.2361111111    1.0\n"
"        0.5000000000    0.7500000000    0.2500000000    1.0\n"
"        0.5000000000    0.7400000000    0.2600000000    1.0\n"
"        0.5000000000    0.7300000000    0.2700000000    1.0\n"
"        0.5000000000    0.7200000000    0.2800000000    1.0\n"
"        0.5000000000    0.7100000000    0.2900000000    1.0\n"
"        0.5000000000    0.7000000000    0.3000000000    1.0\n"
"        0.5000000000    0.6900000000    0.3100000000    1.0\n"
"        0.5000000000    0.6800000000    0.3200000000    1.0\n"
"        0.5000000000    0.6700000000    0.3300000000    1.0\n"
"        0.5000000000    0.6600000000    0.3400000000    1.0\n"
"        0.5000000000    0.6500000000    0.3500000000    1.0\n"
"        0.5000000000    0.6400000000    0.3600000000    1.0\n"
"        0.5000000000    0.6300000000    0.3700000000    1.0\n"
"        0.5000000000    0.6200000000    0.3800000000    1.0\n"
"        0.5000000000    0.6100000000    0.3900000000    1.0\n"
"        0.5000000000    0.6000000000    0.4000000000    1.0\n"
"        0.5000000000    0.5900000000    0.4100000000    1.0\n"
"        0.5000000000    0.5800000000    0.4200000000    1.0\n"
"        0.5000000000    0.5700000000    0.4300000000    1.0\n"
"        0.5000000000    0.5600000000    0.4400000000    1.0\n"
"        0.5000000000    0.5500000000    0.4500000000    1.0\n"
"        0.5000000000    0.5400000000    0.4600000000    1.0\n"
"        0.5000000000    0.5300000000    0.4700000000    1.0\n"
"        0.5000000000    0.5200000000    0.4800000000    1.0\n"
"        0.5000000000    0.5100000000    0.4900000000    1.0\n"
"        0.5000000000    0.5000000000    0.5000000000    1.0\n"
"        0.4838709677    0.4838709677    0.4838709677    1.0\n"
"        0.4677419355    0.4677419355    0.4677419355    1.0\n"
"        0.4516129032    0.4516129032    0.4516129032    1.0\n"
"        0.4354838710    0.4354838710    0.4354838710    1.0\n"
"        0.4193548387    0.4193548387    0.4193548387    1.0\n"
"        0.4032258065    0.4032258065    0.4032258065    1.0\n"
"        0.3870967742    0.3870967742    0.3870967742    1.0\n"
"        0.3709677419    0.3709677419    0.3709677419    1.0\n"
"        0.3548387097    0.3548387097    0.3548387097    1.0\n"
"        0.3387096774    0.3387096774    0.3387096774    1.0\n"
"        0.3225806452    0.3225806452    0.3225806452    1.0\n"
"        0.3064516129    0.3064516129    0.3064516129    1.0\n"
"        0.2903225806    0.2903225806    0.2903225806    1.0\n"
"        0.2741935484    0.2741935484    0.2741935484    1.0\n"
"        0.2580645161    0.2580645161    0.2580645161    1.0\n"
"        0.2419354839    0.2419354839    0.2419354839    1.0\n"
"        0.2258064516    0.2258064516    0.2258064516    1.0\n"
"        0.2096774194    0.2096774194    0.2096774194    1.0\n"
"        0.1935483871    0.1935483871    0.1935483871    1.0\n"
"        0.1774193548    0.1774193548    0.1774193548    1.0\n"
"        0.1612903226    0.1612903226    0.1612903226    1.0\n"
"        0.1451612903    0.1451612903    0.1451612903    1.0\n"
"        0.1290322581    0.1290322581    0.1290322581    1.0\n"
"        0.1129032258    0.1129032258    0.1129032258    1.0\n"
"        0.0967741935    0.0967741935    0.0967741935    1.0\n"
"        0.0806451613    0.0806451613    0.0806451613    1.0\n"
"        0.0645161290    0.0645161290    0.0645161290    1.0\n"
"        0.0483870968    0.0483870968    0.0483870968    1.0\n"
"        0.0322580645    0.0322580645    0.0322580645    1.0\n"
"        0.0161290323    0.0161290323    0.0161290323    1.0\n"
"        0.0000000000    0.0000000000    0.0000000000    1.0 \n"
""))
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

