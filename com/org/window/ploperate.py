# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\workspace\vzplmanager\com\org\ui\ploperate.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!
import mysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from com.org.window.pladdoperate import Ui_AddOperateMainWindow
from com.org.window.plmodifyoperate import Ui_ModifyOperateMainWindow


class Ui_PlOperateForm(object):
    def initdata(self, val):
        self.val = val

    def setupUi(self, PlOperateForm):
        PlOperateForm.setObjectName("PlOperateForm")
        PlOperateForm.resize(94, 23)
        self.toolButton = QtWidgets.QToolButton(PlOperateForm)
        self.toolButton.setGeometry(QtCore.QRect(0, 0, 31, 21))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../window/img/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(PlOperateForm)
        self.toolButton_2.setGeometry(QtCore.QRect(30, 0, 31, 21))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../window/img/modify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(PlOperateForm)
        self.toolButton_3.setGeometry(QtCore.QRect(60, 0, 31, 21))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../window/img/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setObjectName("toolButton_3")

        self.retranslateUi(PlOperateForm)
        QtCore.QMetaObject.connectSlotsByName(PlOperateForm)

    def retranslateUi(self, PlOperateForm):
        _translate = QtCore.QCoreApplication.translate
        PlOperateForm.setWindowTitle(_translate("PlOperateForm", "Form"))
        self.toolButton.setText(_translate("PlOperateForm", "添加"))
        self.toolButton_2.setText(_translate("PlOperateForm", "修改"))
        self.toolButton_3.setText(_translate("PlOperateForm", "删除"))
        self.initslot()

    def initslot(self):
        self.toolButton.clicked.connect(self.add)
        self.toolButton_2.clicked.connect(self.modify)
        self.toolButton_3.clicked.connect(self.delete)


    def initdata(self,val):
        self.val = val

    def add(self):
        self.mainwindow = QtWidgets.QMainWindow()
        self.add = Ui_AddOperateMainWindow()
        self.add.setupUi(self.mainwindow)
        self.add.load(self.val)
        self.mainwindow.show()

    def modify(self):
        self.mainwindow = QtWidgets.QMainWindow()
        self.modify = Ui_ModifyOperateMainWindow()
        self.modify.setupUi(self.mainwindow)
        print ("modify")
        self.modify.load(self.val)
        self.mainwindow.show()

    def delete(self):
        reply = QMessageBox.question(self, 'Message', '确认删除?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            cnx = mysql.connector.connect(user='root', password='qwer1234',
                                          host='127.0.0.1', database='vzplmanager')
            cursor = cnx.cursor()
            step = self.val[3]
            delete = "delete from  record where step = '%s' " % (step)
            cursor.execute(delete)
            cnx.commit()
            cursor.close()
            cnx.close()
            pass


