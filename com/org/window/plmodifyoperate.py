# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\workspace\vzplmanager\com\org\ui\plmodifyoperate.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!
from datetime import datetime

import mysql
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ModifyOperateMainWindow(object):
    def setupUi(self, ModifyOperateMainWindow):
        ModifyOperateMainWindow.setObjectName("ModifyOperateMainWindow")
        ModifyOperateMainWindow.resize(416, 296)
        self.centralwidget = QtWidgets.QWidget(ModifyOperateMainWindow)
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
        ModifyOperateMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ModifyOperateMainWindow)
        self.statusbar.setObjectName("statusbar")
        ModifyOperateMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ModifyOperateMainWindow)
        QtCore.QMetaObject.connectSlotsByName(ModifyOperateMainWindow)

    def retranslateUi(self, ModifyOperateMainWindow):
        _translate = QtCore.QCoreApplication.translate
        ModifyOperateMainWindow.setWindowTitle(_translate("ModifyOperateMainWindow", "MainWindow"))
        self.label.setText(_translate("ModifyOperateMainWindow", "事件处理："))
        self.pushButton.setText(_translate("ModifyOperateMainWindow", "修改"))
        self.pushButton_2.setText(_translate("ModifyOperateMainWindow", "取消"))

    def initslot(self):
        self.pushButton.clicked.connect(self.commit)
        self.pushButton_2.clicked.connect(self.cancel)
        self.textEdit.setText(self.val[3])


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

        update = "update record set body= '%s',partment='%s',eventtype='%s',step='%s',create_time='%s' where step='%s'" % (
        body, partment, eventtype, step, datetime(2017, 3, 18,1,2,34), self.val[3])


        cursor.execute(update)

        cnx.commit()
        cursor.close()
        cnx.close()


    def load(self, val):
        #val = [body, partment, eventtype, step, create_time]

        self.val = val
        self.initslot()