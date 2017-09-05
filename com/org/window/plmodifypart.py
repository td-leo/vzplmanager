# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\workspace\vzplmanager\com\org\ui\plmodifypart.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!
import mysql
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ModifyPartMainWindow(object):
    def setupUi(self, ModifyPartMainWindow):
        ModifyPartMainWindow.setObjectName("ModifyPartMainWindow")
        ModifyPartMainWindow.resize(368, 324)
        self.centralwidget = QtWidgets.QWidget(ModifyPartMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 270, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(140, 40, 191, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 61, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 270, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 61, 20))
        self.label_3.setObjectName("label_3")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(140, 140, 191, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 52, 81, 20))
        self.label.setObjectName("label")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(140, 90, 191, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        ModifyPartMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ModifyPartMainWindow)
        self.statusbar.setObjectName("statusbar")
        ModifyPartMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ModifyPartMainWindow)
        QtCore.QMetaObject.connectSlotsByName(ModifyPartMainWindow)

    def retranslateUi(self, ModifyPartMainWindow):
        _translate = QtCore.QCoreApplication.translate
        ModifyPartMainWindow.setWindowTitle(_translate("ModifyPartMainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("ModifyPartMainWindow", "取消"))
        self.label_2.setText(_translate("ModifyPartMainWindow", "人数："))
        self.pushButton.setText(_translate("ModifyPartMainWindow", "确定"))
        self.label_3.setText(_translate("ModifyPartMainWindow", "预备人员："))
        self.label.setText(_translate("ModifyPartMainWindow", "部门："))

        self.pushButton.clicked.connect(self.commit)
        self.pushButton_2.clicked.connect(self.cancel)

    def commit(self):
        cnx = mysql.connector.connect(user='root', password='qwer1234',
                                      host='127.0.0.1', database='vzplmanager')
        cursor = cnx.cursor()

        partment = self.textEdit.toPlainText()
        count = self.textEdit_2.toPlainText()
        extra_count = self.textEdit_3.toPlainText()

        print (partment, count, extra_count, self.val[0])
        update = "update part set partment= '%s', count='%s', extra_count='%s' where partment='%s'" % (partment, count, extra_count, self.val[0])

        cursor.execute(update)

        cnx.commit()
        cursor.close()
        cnx.close()

    def cancel(self):
        pass

    def load(self, val):
        self.textEdit.setText(val[0])
        self.textEdit_2.setText(val[1])
        self.textEdit_3.setText(val[2])
        self.val = val
