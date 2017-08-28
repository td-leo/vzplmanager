# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!
import mysql
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date, datetime


class Ui_LogForm(object):
    def setupUi(self, LogForm):
        LogForm.setObjectName("LogForm")
        LogForm.resize(729, 449)
        self.tableWidget = QtWidgets.QTableWidget(LogForm)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 581, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.label = QtWidgets.QLabel(LogForm)
        self.label.setGeometry(QtCore.QRect(60, 310, 54, 12))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(LogForm)
        self.textEdit.setGeometry(QtCore.QRect(130, 310, 281, 21))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(LogForm)
        self.textEdit_2.setGeometry(QtCore.QRect(130, 340, 281, 21))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(LogForm)
        self.label_2.setGeometry(QtCore.QRect(60, 340, 54, 12))
        self.label_2.setObjectName("label_2")
        self.textEdit_3 = QtWidgets.QTextEdit(LogForm)
        self.textEdit_3.setGeometry(QtCore.QRect(130, 370, 281, 21))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_3 = QtWidgets.QLabel(LogForm)
        self.label_3.setGeometry(QtCore.QRect(60, 370, 54, 12))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(LogForm)
        self.pushButton.setGeometry(QtCore.QRect(450, 400, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(LogForm)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 400, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget.verticalHeader().setVisible(False)
        self.retranslateUi(LogForm)
        QtCore.QMetaObject.connectSlotsByName(LogForm)

    def retranslateUi(self, LogForm):
        _translate = QtCore.QCoreApplication.translate
        LogForm.setWindowTitle(_translate("LogForm", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("LogForm", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("LogForm", "时间"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("LogForm", "操作"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("LogForm", "目录/文件对象"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("LogForm", "数量"))
        self.label.setText(_translate("LogForm", "CDP时间："))
        self.label_2.setText(_translate("LogForm", "操作："))
        self.label_3.setText(_translate("LogForm", "目录文件："))
        self.pushButton.setText(_translate("LogForm", "确认"))
        self.pushButton_2.setText(_translate("LogForm", "关闭"))

        self.tableWidget.setColumnWidth(0,40)
        self.tableWidget.setColumnWidth(1, 160)
        self.tableWidget.setColumnWidth(2, 60)
        self.tableWidget.setColumnWidth(3, 200)
        self.tableWidget.setColumnWidth(4, 40)

        self.tableWidget.itemClicked.connect(self.onItemClick)
        self.getLog()


    def onItemClick(self):
        ct = self.tableWidget.currentItem().text()
        print(ct)
        cnx = mysql.connector.connect(user='root', password='qwer1234',
                              host='127.0.0.1', database='cloud')
        cursor = cnx.cursor()
        query = ("select operation, restore_date, client_files from log where log_no = '%s'" %ct)
        cursor.execute(query)
        for(operation, restore_date,client_files) in cursor:
            self.textEdit.setText(datetime.strftime(restore_date, '%Y-%m-%d %H:%M:%S'))
            self.textEdit_2.setText(operation)
            self.textEdit_3.setText(client_files)
        print(str(cursor.rowcount))
        if cursor.rowcount == -1:
            self.textEdit.setText("")
            self.textEdit_2.setText("")
            self.textEdit_3.setText("")
        cursor.close()
        cnx.close()



    def getLog(self):
        cnx = mysql.connector.connect(user='root', password='qwer1234',
                              host='127.0.0.1', database='cloud')
        cursor = cnx.cursor()
        query = ("select log_no, operation, restore_date, client_files from log")
        cursor.execute(query)

        self.tableWidget.setRowCount(20)
        for (log_no, operation, restore_date, client_files) in cursor:
            i = cursor.rowcount - 1
            print(i)
            time1_str = datetime.strftime(restore_date, '%Y-%m-%d %H:%M:%S')
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(log_no)))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(time1_str))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(operation))
            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(client_files))
            self.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem('1'))

        cursor.close()
        cnx.close()


    def getFackLog(self):
        for i in range(0, 20):
            self.tableWidget.setItem(i,1 ,QtWidgets.QTableWidgetItem("08-20 16:14:23.548712"))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem("backup"))
            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem("C:/users/pic/->C:/backup"))
            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem("1"))
