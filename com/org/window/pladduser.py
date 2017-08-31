# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\workspace\vzplmanager\com\org\ui\pladduser.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddUserMainWindow(object):
    def setupUi(self, AddUserMainWindow):
        AddUserMainWindow.setObjectName("AddUserMainWindow")
        AddUserMainWindow.resize(318, 313)
        self.centralwidget = QtWidgets.QWidget(AddUserMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 45, 61, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 61, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 140, 61, 21))
        self.label_3.setObjectName("label_3")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(130, 260, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(130, 90, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 140, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(130, 40, 104, 31))
        self.textEdit.setObjectName("textEdit")
        AddUserMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AddUserMainWindow)
        self.statusbar.setObjectName("statusbar")
        AddUserMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddUserMainWindow)
        QtCore.QMetaObject.connectSlotsByName(AddUserMainWindow)

    def retranslateUi(self, AddUserMainWindow):
        _translate = QtCore.QCoreApplication.translate
        AddUserMainWindow.setWindowTitle(_translate("AddUserMainWindow", "MainWindow"))
        self.label.setText(_translate("AddUserMainWindow", "用户姓名："))
        self.label_2.setText(_translate("AddUserMainWindow", "部门："))
        self.label_3.setText(_translate("AddUserMainWindow", "权限："))
        self.comboBox.setItemText(0, _translate("AddUserMainWindow", "后勤科"))
        self.comboBox.setItemText(1, _translate("AddUserMainWindow", "接警处"))
        self.comboBox_2.setItemText(0, _translate("AddUserMainWindow", "管理员"))
        self.comboBox_2.setItemText(1, _translate("AddUserMainWindow", "超级管理员"))

