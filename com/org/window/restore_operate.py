# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'restore_operate.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from com.org.window.dialog_update import Ui_Dialog

class RestoreDialog(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self):
        super(RestoreDialog, self).__init__()
        self.setupUi(self)


class Ui_RestoreOperateForm(object):
    def setupUi(self, RestoreOperateForm):
        RestoreOperateForm.setObjectName("RestoreOperateForm")
        RestoreOperateForm.resize(113, 24)
        self.pushButton = QtWidgets.QPushButton(RestoreOperateForm)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 31, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(RestoreOperateForm)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 0, 31, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(RestoreOperateForm)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 0, 31, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton.clicked.connect(self.onRestore)

        self.retranslateUi(RestoreOperateForm)
        QtCore.QMetaObject.connectSlotsByName(RestoreOperateForm)

    def onRestore(self):
        restore = RestoreDialog()
        restore.show()

    def retranslateUi(self, RestoreOperateForm):
        _translate = QtCore.QCoreApplication.translate
        RestoreOperateForm.setWindowTitle(_translate("RestoreOperateForm", "Form"))
        self.pushButton.setText(_translate("RestoreOperateForm", "恢复"))
        self.pushButton_2.setText(_translate("RestoreOperateForm", "浏览云端数据"))
        self.pushButton_3.setText(_translate("RestoreOperateForm", "查看存储空间"))

