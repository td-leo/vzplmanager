# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\workspace\vzplmanager\com\org\ui\plmodifyuser.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!
import datetime
import mysql
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ModiyfUserMainWindow(object):
    def setupUi(self, ModiyfUserMainWindow):
        ModiyfUserMainWindow.setObjectName("ModiyfUserMainWindow")
        ModiyfUserMainWindow.resize(400, 320)
        self.centralwidget = QtWidgets.QWidget(ModiyfUserMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 270, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(150, 90, 191, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 52, 81, 20))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(150, 40, 191, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 270, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 61, 20))
        self.label_2.setObjectName("label_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(150, 140, 191, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 150, 61, 20))
        self.label_3.setObjectName("label_3")
        ModiyfUserMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ModiyfUserMainWindow)
        self.statusbar.setObjectName("statusbar")
        ModiyfUserMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ModiyfUserMainWindow)
        QtCore.QMetaObject.connectSlotsByName(ModiyfUserMainWindow)

    def retranslateUi(self, ModiyfUserMainWindow):
        _translate = QtCore.QCoreApplication.translate
        ModiyfUserMainWindow.setWindowTitle(_translate("ModiyfUserMainWindow", "MainWindow"))
        self.pushButton.setText(_translate("ModiyfUserMainWindow", "确定"))
        self.label.setText(_translate("ModiyfUserMainWindow", "账号："))
        self.pushButton_2.setText(_translate("ModiyfUserMainWindow", "取消"))
        self.label_2.setText(_translate("ModiyfUserMainWindow", "用户名称："))
        self.label_3.setText(_translate("ModiyfUserMainWindow", "部门："))

        self.pushButton.clicked.connect(self.commit)
        self.pushButton_2.clicked.connect(self.cancel)


    def commit(self):
        cnx = mysql.connector.connect(user='root', password='qwer1234',
                              host='127.0.0.1', database='vzplmanager')
        cursor = cnx.cursor()
        username = self.textEdit_2.toPlainText()
        account = self.textEdit.toPlainText()
        partment = self.textEdit_3.toPlainText()

        print(username, account,partment, self.val[2])
        update = "update user set username= '%s', account='%s', partment='%s' where username ='%s'" %(username, account, partment, self.val[2])
        cursor.execute(update)

        cnx.commit()
        cursor.close()
        cnx.close()

    def cancel(self):
        pass

    def load(self, val):
        self.textEdit.setText(val[0])
        self.textEdit_2.setText(val[2])
        self.textEdit_3.setText(val[3])
        self.val = val

