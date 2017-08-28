# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'backup_operate.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BackupOperateForm(object):
    def setupUi(self, BackupOperateForm):
        BackupOperateForm.setObjectName("BackupOperateForm")
        BackupOperateForm.resize(191, 23)
        self.pushButton = QtWidgets.QPushButton(BackupOperateForm)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 31, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(BackupOperateForm)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 0, 31, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(BackupOperateForm)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 0, 31, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(BackupOperateForm)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 0, 31, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(BackupOperateForm)
        self.pushButton_5.setGeometry(QtCore.QRect(160, 0, 31, 23))
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(BackupOperateForm)
        QtCore.QMetaObject.connectSlotsByName(BackupOperateForm)

    def retranslateUi(self, BackupOperateForm):
        _translate = QtCore.QCoreApplication.translate
        BackupOperateForm.setWindowTitle(_translate("BackupOperateForm", "Form"))
        self.pushButton.setText(_translate("BackupOperateForm", "开始"))
        self.pushButton_2.setText(_translate("BackupOperateForm", "停止"))
        self.pushButton_3.setText(_translate("BackupOperateForm", "查看云端空间"))
        self.pushButton_4.setText(_translate("BackupOperateForm", "异常"))
        self.pushButton_5.setText(_translate("BackupOperateForm", "失效"))

