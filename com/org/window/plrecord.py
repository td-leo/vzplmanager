# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\workspace\vzplmanager\com\org\ui\plrecord.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PlRecordForm(object):
    def setupUi(self, PlRecordForm):
        PlRecordForm.setObjectName("PlRecordForm")
        PlRecordForm.resize(632, 469)
        self.tableWidget = QtWidgets.QTableWidget(PlRecordForm)
        self.tableWidget.setGeometry(QtCore.QRect(10, 90, 611, 371))
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.graphicsView = QtWidgets.QGraphicsView(PlRecordForm)
        self.graphicsView.setGeometry(QtCore.QRect(10, 20, 151, 51))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(PlRecordForm)
        self.label.setGeometry(QtCore.QRect(190, 40, 61, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(PlRecordForm)
        self.label_2.setGeometry(QtCore.QRect(370, 40, 91, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(PlRecordForm)
        self.pushButton.setGeometry(QtCore.QRect(480, 40, 75, 23))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(PlRecordForm)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 40, 75, 23))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(PlRecordForm)
        QtCore.QMetaObject.connectSlotsByName(PlRecordForm)

    def retranslateUi(self, PlRecordForm):
        _translate = QtCore.QCoreApplication.translate
        PlRecordForm.setWindowTitle(_translate("PlRecordForm", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("PlRecordForm", "报警时间"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("PlRecordForm", "内容"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("PlRecordForm", "单位"))
        self.label.setText(_translate("PlRecordForm", "自动接警："))
        self.label_2.setText(_translate("PlRecordForm", "接受已失效报警:"))

