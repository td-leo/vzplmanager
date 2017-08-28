# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'query.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!
from datetime import datetime

import mysql
from PyQt5 import QtCore, QtGui, QtWidgets

from com.org.window.settings import OperateForm, RestoreOperateForm, ProgressForm, RestoringOperateForm


class Ui_QueryForm(object):
    def setupUi(self, Form):
        Form.setObjectName("QueryForm")
        Form.resize(729, 448)
        self.ClientTable = QtWidgets.QTableWidget(Form)
        self.ClientTable.setGeometry(QtCore.QRect(20, 50, 701, 381))
        self.ClientTable.setObjectName("ClientTable")
        self.ClientTable.setColumnCount(5)

        item = QtWidgets.QTableWidgetItem()
        self.ClientTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ClientTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ClientTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ClientTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ClientTable.setHorizontalHeaderItem(4, item)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 20, 51, 23))
        self.pushButton_2.setObjectName("pushButton_2")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.ClientTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "状态"))
        item = self.ClientTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "恢复任务名称"))
        item = self.ClientTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "恢复客户端目录/文件"))
        item = self.ClientTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "创建时间"))
        item = self.ClientTable.horizontalHeaderItem(4)
        item.setText(_translate("Form", "操作"))
        self.pushButton_2.setText(_translate("Form", "刷新"))
        white = 'FFFFFF'
        blue = '1C86EE'
        style = """
                QPushButton {
                    border: 1px solid grey;
                    border-radius: 5px;
                    text-align: center;
                    color: #%s;
                    background-color: #%s;
                }""" % (white, blue)
        self.pushButton_2.setStyleSheet(style)
        self.ClientTable.setColumnWidth(0,90)
        self.ClientTable.setColumnWidth(1, 90)
        self.ClientTable.setColumnWidth(2, 130)
        self.ClientTable.setColumnWidth(3, 150)
        self.ClientTable.setColumnWidth(4, 200)
        self.getRecord()

    def showRestoreRecord(self, client_name):
        cnx = mysql.connector.connect(user='root', password='qwer1234',
                              host='127.0.0.1', database='cloud')
        cursor = cnx.cursor()
        query_record = ("select client_name, restore_type, client_files, restore_date from log where client_name='%s'"%client_name)
        cursor.execute(query_record)
        for(client_name, restore_type, client_files, restore_date) in cursor:
            self.ClientTable.insertRow(self.num)
            restore_operate = RestoringOperateForm()
            progressbar = ProgressForm()
            restore_operate.pushButton.clicked.connect(progressbar.onStart)
            restore_operate.pushButton_2.clicked.connect(progressbar.onStop)

            self.ClientTable.setCellWidget(self.num, 0, progressbar)
            self.ClientTable.setItem(self.num, 1, QtWidgets.QTableWidgetItem(restore_type))
            self.ClientTable.setItem(self.num, 2, QtWidgets.QTableWidgetItem(client_files))
            time1_str = datetime.strftime(restore_date, '%Y-%m-%d %H:%M:%S')
            self.ClientTable.setItem(self.num, 3, QtWidgets.QTableWidgetItem(time1_str))
            self.ClientTable.setCellWidget(self.num, 4, restore_operate)
            self.num += 1
        cursor.close()
        cnx.close()

    def showClient(self, client_name, ipaddress, clouddir):
        i = self.num
        print("client_name:" +client_name +"  :" +str(i))
        operate = RestoreOperateForm()
        str1 = "客户端：" + client_name + " | " + "地址：" + ipaddress + " | " + "备份根目录：" + clouddir
        self.ClientTable.insertRow(i)
        self.ClientTable.setSpan(i, 1, 1, 3)
        self.ClientTable.setItem(i, 1, QtWidgets.QTableWidgetItem(str1))
        self.ClientTable.setCellWidget(i, 4, operate)
        self.num += 1

    def getRecord(self):
        cnx = mysql.connector.connect(user='root', password='qwer1234',
                              host='127.0.0.1', database='cloud')
        cursor = cnx.cursor()
        query = ("select client_name, ipaddress, clouddir from client")
        cursor.execute(query)
        self.num = 0
        for (client_name, ipaddress, clouddir) in cursor:
            self.showClient(client_name, ipaddress, clouddir)
            self.showRestoreRecord(client_name)

        cursor.close()
        cnx.close()

