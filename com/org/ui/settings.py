# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SetingsForm(object):
    def setupUi(self, SetingsForm):
        SetingsForm.setObjectName("SetingsForm")
        SetingsForm.resize(728, 448)
        self.pushButton = QtWidgets.QPushButton(SetingsForm)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(SetingsForm)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 10, 51, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.ClientTable = QtWidgets.QTableWidget(SetingsForm)
        self.ClientTable.setGeometry(QtCore.QRect(20, 40, 701, 401))
        self.ClientTable.setObjectName("ClientTable")
        self.ClientTable.setColumnCount(5)
        self.ClientTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ClientTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ClientTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ClientTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ClientTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ClientTable.setHorizontalHeaderItem(4, item)
        self.progressBar = QtWidgets.QProgressBar(SetingsForm)
        self.progressBar.setGeometry(QtCore.QRect(250, 200, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(SetingsForm)
        self.pushButton.clicked.connect(SetingsForm.onNewClick)
        self.pushButton_2.clicked.connect(self.progressBar.reset)
        QtCore.QMetaObject.connectSlotsByName(SetingsForm)

    def retranslateUi(self, SetingsForm):
        _translate = QtCore.QCoreApplication.translate
        SetingsForm.setWindowTitle(_translate("SetingsForm", "Form"))
        self.pushButton.setText(_translate("SetingsForm", "新建客户端"))
        self.pushButton_2.setText(_translate("SetingsForm", "刷新"))
        item = self.ClientTable.horizontalHeaderItem(0)
        item.setText(_translate("SetingsForm", "状态"))
        item = self.ClientTable.horizontalHeaderItem(1)
        item.setText(_translate("SetingsForm", "备份规则名称"))
        item = self.ClientTable.horizontalHeaderItem(2)
        item.setText(_translate("SetingsForm", "客户端目录/文件"))
        item = self.ClientTable.horizontalHeaderItem(3)
        item.setText(_translate("SetingsForm", "云端目标文件"))
        item = self.ClientTable.horizontalHeaderItem(4)
        item.setText(_translate("SetingsForm", "操作"))

