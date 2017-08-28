# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'infomation.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InfoForm(object):
    def setupUi(self, InfoForm):
        InfoForm.setObjectName("InfoForm")
        InfoForm.resize(724, 449)
        self.label = QtWidgets.QLabel(InfoForm)
        self.label.setGeometry(QtCore.QRect(50, 5, 31, 20))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(InfoForm)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(110, 6, 151, 20))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(InfoForm)
        self.textEdit_2.setEnabled(False)
        self.textEdit_2.setGeometry(QtCore.QRect(110, 35, 151, 21))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(InfoForm)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 51, 31))
        self.label_2.setObjectName("label_2")
        self.textEdit_3 = QtWidgets.QTextEdit(InfoForm)
        self.textEdit_3.setEnabled(False)
        self.textEdit_3.setGeometry(QtCore.QRect(110, 65, 151, 21))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_3 = QtWidgets.QLabel(InfoForm)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 61, 31))
        self.label_3.setObjectName("label_3")
        self.textEdit_4 = QtWidgets.QTextEdit(InfoForm)
        self.textEdit_4.setEnabled(False)
        self.textEdit_4.setGeometry(QtCore.QRect(440, 10, 151, 20))
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_4 = QtWidgets.QLabel(InfoForm)
        self.label_4.setGeometry(QtCore.QRect(340, 10, 81, 20))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(InfoForm)
        QtCore.QMetaObject.connectSlotsByName(InfoForm)

    def retranslateUi(self, InfoForm):
        _translate = QtCore.QCoreApplication.translate
        InfoForm.setWindowTitle(_translate("InfoForm", "Form"))
        self.label.setText(_translate("InfoForm", "用户："))
        self.label_2.setText(_translate("InfoForm", "注册邮件："))
        self.label_3.setText(_translate("InfoForm", "密钥认证："))
        self.label_4.setText(_translate("InfoForm", "上次登录时间："))

