# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\workspace\vzplmanager\com\org\ui\plmodifypermission.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!
import mysql
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ModifyPermissionMainWindow(object):
    def setupUi(self, ModifyPermissionMainWindow):
        ModifyPermissionMainWindow.setObjectName("ModifyPermissionMainWindow")
        ModifyPermissionMainWindow.resize(453, 337)
        self.centralwidget = QtWidgets.QWidget(ModifyPermissionMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 62, 81, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 61, 20))
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(180, 50, 191, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(180, 100, 191, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 280, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 280, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        ModifyPermissionMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ModifyPermissionMainWindow)
        self.statusbar.setObjectName("statusbar")
        ModifyPermissionMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ModifyPermissionMainWindow)
        QtCore.QMetaObject.connectSlotsByName(ModifyPermissionMainWindow)

    def retranslateUi(self, ModifyPermissionMainWindow):
        _translate = QtCore.QCoreApplication.translate
        ModifyPermissionMainWindow.setWindowTitle(_translate("ModifyPermissionMainWindow", "MainWindow"))
        self.label.setText(_translate("ModifyPermissionMainWindow", "权限编号："))
        self.label_2.setText(_translate("ModifyPermissionMainWindow", "权限名称："))
        self.pushButton.setText(_translate("ModifyPermissionMainWindow", "确定"))
        self.pushButton_2.setText(_translate("ModifyPermissionMainWindow", "取消"))

        self.pushButton.clicked.connect(self.commit)
        self.pushButton_2.clicked.connect(self.cancel)


    def commit(self):
        cnx = mysql.connector.connect(user='root', password='qwer1234',
                              host='127.0.0.1', database='vzplmanager')
        cursor = cnx.cursor()

        value = self.textEdit.toPlainText()
        account = self.textEdit_2.toPlainText()
        update = "update permission set value= '%s', account='%s' where account = '%s'" %(value, account, self.account )

        cursor.execute(update)

        cnx.commit()
        cursor.close()
        cnx.close()

    def cancel(self):
        pass

    def load(self, val):
        self.val = val
        self.textEdit.setText(val[1])
        self.textEdit_2.setText(val[2])
        self.account = val[2]






