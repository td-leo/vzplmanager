# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\workspace\vzplmanager\com\org\ui\ploperate.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PlOperateForm(object):
    def setupUi(self, PlOperateForm):
        PlOperateForm.setObjectName("PlOperateForm")
        PlOperateForm.resize(94, 23)
        self.toolButton = QtWidgets.QToolButton(PlOperateForm)
        self.toolButton.setGeometry(QtCore.QRect(0, 0, 31, 21))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../window/img/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(PlOperateForm)
        self.toolButton_2.setGeometry(QtCore.QRect(30, 0, 31, 21))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../window/img/modify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(PlOperateForm)
        self.toolButton_3.setGeometry(QtCore.QRect(60, 0, 31, 21))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../window/img/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setObjectName("toolButton_3")

        self.retranslateUi(PlOperateForm)
        QtCore.QMetaObject.connectSlotsByName(PlOperateForm)

    def retranslateUi(self, PlOperateForm):
        _translate = QtCore.QCoreApplication.translate
        PlOperateForm.setWindowTitle(_translate("PlOperateForm", "Form"))
        self.toolButton.setText(_translate("PlOperateForm", "添加"))
        self.toolButton_2.setText(_translate("PlOperateForm", "修改"))
        self.toolButton_3.setText(_translate("PlOperateForm", "删除"))

