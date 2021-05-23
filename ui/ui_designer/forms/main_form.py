# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_form.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(458, 372)
        self.textEdit = QtWidgets.QTextEdit(MainForm)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 104, 321))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(MainForm)
        self.pushButton.setGeometry(QtCore.QRect(130, 40, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Batch Ping by Tanyiqu"))
        self.pushButton.setText(_translate("MainForm", "Ping"))
