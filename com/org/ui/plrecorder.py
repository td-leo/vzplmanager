# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\workspace\vzplmanager\com\org\ui\plrecorder.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RecorderForm(object):
    def setupUi(self, RecorderForm):
        RecorderForm.setObjectName("RecorderForm")
        RecorderForm.resize(961, 487)
        self.tableWidget = QtWidgets.QTableWidget(RecorderForm)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 931, 401))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.label = QtWidgets.QLabel(RecorderForm)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(RecorderForm)
        self.pushButton.setGeometry(QtCore.QRect(640, 400, 21, 21))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../window/img/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(23, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(RecorderForm)
        QtCore.QMetaObject.connectSlotsByName(RecorderForm)

    def retranslateUi(self, RecorderForm):
        _translate = QtCore.QCoreApplication.translate
        RecorderForm.setWindowTitle(_translate("RecorderForm", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("RecorderForm", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("RecorderForm", "案件"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("RecorderForm", "接警员"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("RecorderForm", "播放"))
        self.label.setText(_translate("RecorderForm", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#4a4a4a;\">查看接警录音：</span></p></body></html>"))

