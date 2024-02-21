# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Get2dMaterialData.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ScrollArea(object):
    def setupUi(self, ScrollArea):
        ScrollArea.setObjectName("ScrollArea")
        ScrollArea.resize(505, 190)
        ScrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 502, 187))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_MainHeading = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_MainHeading.setGeometry(QtCore.QRect(170, 3, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_MainHeading.setFont(font)
        self.label_MainHeading.setMouseTracking(False)
        self.label_MainHeading.setObjectName("label_MainHeading")
        self.label_MaterialName = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_MaterialName.setGeometry(QtCore.QRect(10, 30, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_MaterialName.setFont(font)
        self.label_MaterialName.setObjectName("label_MaterialName")
        self.label_LatticeParameter = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_LatticeParameter.setGeometry(QtCore.QRect(10, 60, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_LatticeParameter.setFont(font)
        self.label_LatticeParameter.setObjectName("label_LatticeParameter")
        self.lineEdit_MaterialName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_MaterialName.setGeometry(QtCore.QRect(250, 30, 241, 21))
        self.lineEdit_MaterialName.setObjectName("lineEdit_MaterialName")
        self.lineEdit_LatticeParameter = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_LatticeParameter.setGeometry(QtCore.QRect(250, 60, 241, 23))
        self.lineEdit_LatticeParameter.setObjectName("lineEdit_LatticeParameter")
        self.pushButton_AddData = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_AddData.setGeometry(QtCore.QRect(130, 100, 80, 23))
        self.pushButton_AddData.setObjectName("pushButton_AddData")
        self.pushButton_Exit = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_Exit.setGeometry(QtCore.QRect(220, 100, 80, 23))
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.pushButton_Overwrite = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_Overwrite.setEnabled(False)
        self.pushButton_Overwrite.setGeometry(QtCore.QRect(310, 100, 80, 23))
        self.pushButton_Overwrite.setObjectName("pushButton_Overwrite")
        self.label_Message = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_Message.setEnabled(True)
        self.label_Message.setGeometry(QtCore.QRect(10, 130, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_Message.setFont(font)
        self.label_Message.setText("")
        self.label_Message.setObjectName("label_Message")
        ScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(ScrollArea)
        QtCore.QMetaObject.connectSlotsByName(ScrollArea)

    def retranslateUi(self, ScrollArea):
        _translate = QtCore.QCoreApplication.translate
        ScrollArea.setWindowTitle(_translate("ScrollArea", "ScrollArea"))
        self.label_MainHeading.setText(_translate("ScrollArea", "2D Materials Data"))
        self.label_MaterialName.setText(_translate("ScrollArea", "Material Name by symbol (ex. MoS2)"))
        self.label_LatticeParameter.setText(_translate("ScrollArea", "Lattice Parameter (in angstrom)"))
        self.pushButton_AddData.setText(_translate("ScrollArea", "Add Data"))
        self.pushButton_Exit.setText(_translate("ScrollArea", "Exit"))
        self.pushButton_Overwrite.setText(_translate("ScrollArea", "Overwrite"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ScrollArea = QtWidgets.QScrollArea()
    ui = Ui_ScrollArea()
    ui.setupUi(ScrollArea)
    ScrollArea.show()
    sys.exit(app.exec_())

