# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\workspace\vzplmanager\com\org\ui\pladdpart.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!
import datetime
import mysql
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddPartMainWindow(object):
    def setupUi(self, AddPartMainWindow):
        AddPartMainWindow.setObjectName("AddPartMainWindow")
        AddPartMainWindow.resize(380, 333)
        self.centralwidget = QtWidgets.QWidget(AddPartMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(150, 130, 191, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 260, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(150, 30, 191, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(150, 80, 191, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 61, 20))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 42, 81, 20))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 260, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 61, 20))
        self.label_3.setObjectName("label_3")
        AddPartMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddPartMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 23))
        self.menubar.setObjectName("menubar")
        AddPartMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddPartMainWindow)
        self.statusbar.setObjectName("statusbar")
        AddPartMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddPartMainWindow)
        QtCore.QMetaObject.connectSlotsByName(AddPartMainWindow)

    def retranslateUi(self, AddPartMainWindow):
        _translate = QtCore.QCoreApplication.translate
        AddPartMainWindow.setWindowTitle(_translate("AddPartMainWindow", "MainWindow"))
        self.pushButton.setText(_translate("AddPartMainWindow", "确定"))
        self.label_2.setText(_translate("AddPartMainWindow", "人数："))
        self.label.setText(_translate("AddPartMainWindow", "部门："))
        self.pushButton_2.setText(_translate("AddPartMainWindow", "取消"))
        self.label_3.setText(_translate("AddPartMainWindow", "预备人员："))

        self.initslot()

    def initslot(self):
        self.pushButton.clicked.connect(self.commit)
        self.pushButton_2.clicked.connect(self.cancel)

    def commit(self):
        partment = self.textEdit.toPlainText()
        count = self.textEdit_3.toPlainText()
        extra_count = self.textEdit_3.toPlainText()

        cnx = mysql.connector.connect(user='root', password='qwer1234',
                              host='127.0.0.1', database='vzplmanager')
        self.cursor = cnx.cursor()

        insert = ("INSERT INTO part "
                        "(partment, count, extra_count)"
                        "VALUES ( %s, %s, %s)")
        vl = (partment, count, extra_count)
        self.cursor.execute(insert, vl)

        cnx.commit()
        self.cursor.close()
        cnx.close()

    def cancel(self):
        pass