# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'restoring_operate.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RestoringOperateForm(object):
    def setupUi(self, RestoringOperateForm):
        RestoringOperateForm.setObjectName("RestoringOperateForm")
        RestoringOperateForm.resize(152, 22)
        self.pushButton = QtWidgets.QPushButton(RestoringOperateForm)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 31, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(RestoringOperateForm)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 0, 31, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(RestoringOperateForm)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 0, 31, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(RestoringOperateForm)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 0, 31, 23))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(RestoringOperateForm)
        QtCore.QMetaObject.connectSlotsByName(RestoringOperateForm)

    def retranslateUi(self, RestoringOperateForm):
        _translate = QtCore.QCoreApplication.translate
        RestoringOperateForm.setWindowTitle(_translate("RestoringOperateForm", "Form"))
        self.pushButton.setText(_translate("RestoringOperateForm", "开始"))
        self.pushButton_2.setText(_translate("RestoringOperateForm", "停止"))
        self.pushButton_3.setText(_translate("RestoringOperateForm", "失效"))
        self.pushButton_4.setText(_translate("RestoringOperateForm", "异常"))

