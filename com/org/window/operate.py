# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'operate.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OperateForm(object):
    def setupUi(self, OperateForm):
        OperateForm.setObjectName("OperateForm")
        OperateForm.resize(113, 22)
        self.pushButton = QtWidgets.QPushButton(OperateForm)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 31, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(OperateForm)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 0, 31, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(OperateForm)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 0, 31, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(OperateForm)
        QtCore.QMetaObject.connectSlotsByName(OperateForm)

    def retranslateUi(self, OperateForm):
        _translate = QtCore.QCoreApplication.translate
        OperateForm.setWindowTitle(_translate("OperateForm", "Form"))
        self.pushButton.setText(_translate("OperateForm", "规则"))
        self.pushButton_2.setText(_translate("OperateForm", "迁移"))
        self.pushButton_3.setText(_translate("OperateForm", "查看云端数据"))

