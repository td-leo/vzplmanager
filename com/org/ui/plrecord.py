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
        PlRecordForm.resize(960, 490)
        self.tableWidget = QtWidgets.QTableWidget(PlRecordForm)
        self.tableWidget.setGeometry(QtCore.QRect(10, 90, 941, 381))
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
        self.label = QtWidgets.QLabel(PlRecordForm)
        self.label.setGeometry(QtCore.QRect(190, 40, 61, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(PlRecordForm)
        self.label_2.setGeometry(QtCore.QRect(330, 40, 91, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(PlRecordForm)
        self.pushButton.setGeometry(QtCore.QRect(420, 40, 51, 23))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../window/img/of.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(53, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(PlRecordForm)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 40, 51, 21))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../window/img/on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(53, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(PlRecordForm)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 54, 51))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../window/img/policylogo.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(PlRecordForm)
        self.label_4.setGeometry(QtCore.QRect(70, 30, 81, 41))
        self.label_4.setLineWidth(0)
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setContentsMargins(2, 2, 2, 2)
        self.label_4.setObjectName("label_4")

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
        self.label_4.setText(_translate("PlRecordForm", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">报警信息</span></p></body></html>"))

