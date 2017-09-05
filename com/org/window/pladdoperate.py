# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\workspace\vzplmanager\com\org\ui\pladdoperate.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!
from datetime import datetime

import mysql
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddOperateMainWindow(object):
    def setupUi(self, AddOperateMainWindow):
        AddOperateMainWindow.setObjectName("AddOperateMainWindow")
        AddOperateMainWindow.resize(416, 296)
        self.centralwidget = QtWidgets.QWidget(AddOperateMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 61, 16))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 50, 341, 161))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 250, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 250, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        AddOperateMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AddOperateMainWindow)
        self.statusbar.setObjectName("statusbar")
        AddOperateMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddOperateMainWindow)
        QtCore.QMetaObject.connectSlotsByName(AddOperateMainWindow)

    def retranslateUi(self, AddOperateMainWindow):
        _translate = QtCore.QCoreApplication.translate
        AddOperateMainWindow.setWindowTitle(_translate("AddOperateMainWindow", "MainWindow"))
        self.label.setText(_translate("AddOperateMainWindow", "事件处理："))
        self.pushButton.setText(_translate("AddOperateMainWindow", "提交"))
        self.pushButton_2.setText(_translate("AddOperateMainWindow", "取消"))

    def initslot(self):
        self.pushButton.clicked.connect(self.commit)
        self.pushButton_2.clicked.connect(self.cancel)


    def cancel(self):
        pass

    def commit(self):
        cnx = mysql.connector.connect(user='root', password='qwer1234',
                              host='127.0.0.1', database='vzplmanager')
        cursor = cnx.cursor()

        body = self.val[0]
        partment =self.val[1]
        eventtype = self.val[2]

        step = self.textEdit.toPlainText()
        add_client = ("INSERT INTO record "
                        "(body, partment, eventtype, step,create_time) "
                        "VALUES ( %s, %s, %s, %s, %s)")

        data_client1 = (body,  partment, eventtype,
                        step,
                        datetime(2017, 3, 18,1,2,34))

        cursor.execute(add_client, data_client1)

        cnx.commit()
        cursor.close()
        cnx.close()


    def load(self, val):
        #val = [body, partment, eventtype, step, create_time]
        self.val = val
        self.initslot()



