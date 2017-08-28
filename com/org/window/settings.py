# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QBasicTimer

from com.org.sql.SqlUtils import SqlUtils
from com.org.window.backup_operate import Ui_BackupOperateForm
from com.org.window.helpcenter.version import Ui_VersionForm
from com.org.window.operate import Ui_OperateForm
import mysql.connector
import sys
from com.org.window.new_client import MainWindow
from com.org.window.progress import Ui_ProgressForm
from com.org.window.restore_operate import Ui_RestoreOperateForm
from com.org.window.dialog_update import Ui_Dialog
from com.org.window.restoring_operate import Ui_RestoringOperateForm
from com.org.window.rules import Ui_RulesForm


class RestoringOperateForm(QtWidgets.QWidget, Ui_RestoringOperateForm):
    def __init__(self):
        super(RestoringOperateForm, self).__init__()
        self.setupUi(self)

class OperateForm(QtWidgets.QWidget, Ui_OperateForm):
    def __init__(self):
        super(OperateForm, self).__init__()
        self.setupUi(self)

class ProgressForm(QtWidgets.QWidget, Ui_ProgressForm):
    def __init__(self):
        super(ProgressForm, self).__init__()
        self.setupUi(self)

class BackupOperateForm(QtWidgets.QWidget, Ui_BackupOperateForm):
    def __init__(self):
        super(BackupOperateForm, self).__init__()
        self.setupUi(self)

class RestoreOperateForm(QtWidgets.QWidget, Ui_RestoreOperateForm):
    def __init__(self):
        super(RestoreOperateForm, self).__init__()
        self.setupUi(self)

class Ui_SetingsForm(object):
    def setupUi(self, SetingsForm):
        SetingsForm.setObjectName("SetingsForm")
        SetingsForm.resize(728, 448)
        self.pushButton = QtWidgets.QPushButton(SetingsForm)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(SetingsForm)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 10, 51, 23))
        self.pushButton_2.setObjectName("pushButton_2")

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
        self.pushButton.setStyleSheet(style)
        self.ClientTable = QtWidgets.QTableWidget(SetingsForm)
        self.ClientTable.setGeometry(QtCore.QRect(20, 40, 701, 401))
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
        self.step = 0
        self.retranslateUi(SetingsForm)
        self.pushButton.clicked.connect(self.onNewClick)
        self.pushButton_2.clicked.connect(self.onRefreshClick)

        QtCore.QMetaObject.connectSlotsByName(SetingsForm)

    def retranslateUi(self, SetingsForm):
        _translate = QtCore.QCoreApplication.translate
        SetingsForm.setWindowTitle(_translate("SetingsForm", "Form"))
        self.pushButton.setText(_translate("SetingsForm", "新建客户端"))
        self.pushButton_2.setText(_translate("SetingsForm", "刷新"))
        item = self.ClientTable.horizontalHeaderItem(0)
        item.setText(_translate("SetingsForm", "状态"))
        self.ClientTable.setColumnWidth(0,90)
        self.ClientTable.setColumnWidth(1, 90)
        self.ClientTable.setColumnWidth(2, 160)
        self.ClientTable.setColumnWidth(3, 120)
        self.ClientTable.setColumnWidth(4, 200)
        item = self.ClientTable.horizontalHeaderItem(1)
        item.setText(_translate("SetingsForm", "备份规则名称"))
        item = self.ClientTable.horizontalHeaderItem(2)
        item.setText(_translate("SetingsForm", "客户端目录/文件"))
        item = self.ClientTable.horizontalHeaderItem(3)
        item.setText(_translate("SetingsForm", "云端目标文件"))
        item = self.ClientTable.horizontalHeaderItem(4)
        item.setText(_translate("SetingsForm", "操作"))
        self.getClient()

    def onNewClick(self):
        self.mainwindow = QtWidgets.QMainWindow()
        self.new_client = MainWindow()
        self.new_client.setupUi(self.mainwindow)
        self.mainwindow.show()

    def onRefreshClick(self):
        self.cp = CProcessBar()
        self.cp.init()


    def openRules(self, client_name):
        self.ruls = RulesForm()
        self.ruls.pushButton_2.clicked.connect(self.rulesSubmit)

    def rulesSubmit(self):
        if self.ruls.checkBox_12.isChecked():
            week = self.ruls.checkBox_12.text()
        if self.ruls.checkBox_13.isChecked():
            week = self.ruls.checkBox_13.text()
        if self.ruls.checkBox_14.isChecked():
            week = self.ruls.checkBox_14.text()
        if self.ruls.checkBox_15.isChecked():
            week = self.ruls.checkBox_15.text()
        if self.ruls.checkBox_16.isChecked():
            week = self.ruls.checkBox_15.text()
        if self.ruls.checkBox_16.isChecked():
            week = self.ruls.checkBox_16.text()
        if self.ruls.checkBox_17.isChecked():
            week = self.ruls.checkBox_17.text()



    def showClient(self, client_name, ipaddress, package):

        i =self.num
        print("client_name:" +client_name +"  :" +str(i))
        operate = OperateForm()
        #operate.pushButton.clicked.connect(self.openRules(client_name))
        str1 = "客户端：" + client_name + " | " + "地址：" + ipaddress + " | " + package
        self.ClientTable.insertRow(i)
        self.ClientTable.setSpan(i, 1, 1, 3)
        self.ClientTable.setItem(i, 1, QtWidgets.QTableWidgetItem(str1))
        self.ClientTable.setCellWidget(i, 4, operate)
        self.num += 1

    def showClientRecord(self, client_name):
        cnx = mysql.connector.connect(user='root', password='qwer1234',
                              host='127.0.0.1', database='cloud')
        cursor = cnx.cursor()
        query_record = ("select client_name, backup_name, client_files, clouddir from backup_record where client_name='%s'"%client_name)
        cursor.execute(query_record)
        for(client_name, backup_name, client_files, clouddir) in cursor:
            self.ClientTable.insertRow(self.num)
            backup_operate = BackupOperateForm()
            progressbar = ProgressForm()
            backup_operate.pushButton.clicked.connect(progressbar.onStart)
            backup_operate.pushButton_2.clicked.connect(progressbar.onStop)

            print("backup_name:" + backup_name+"  :" + str(self.num))
            self.ClientTable.setCellWidget(self.num, 0, progressbar)
            self.ClientTable.setItem(self.num, 1, QtWidgets.QTableWidgetItem(backup_name))
            self.ClientTable.setItem(self.num, 2, QtWidgets.QTableWidgetItem(client_files))
            self.ClientTable.setItem(self.num, 3, QtWidgets.QTableWidgetItem(clouddir))
            self.ClientTable.setCellWidget(self.num, 4, backup_operate)
            self.num += 1
        cursor.close()
        cnx.close()

    def onStart(self):
        self.progressbar.timer.start()

    def getClient(self):
        cnx = mysql.connector.connect(user='root', password='qwer1234',
                              host='127.0.0.1', database='cloud')
        cursor = cnx.cursor()
        query = ("select client_name, ipaddress, package from client")

        cursor.execute(query)
        count = 0
        self.num = 0
        for (client_name, ipaddress, package) in cursor:
            self.showClient(client_name, ipaddress, package)
            self.showClientRecord(client_name)

        cursor.close()
        cnx.close()

    def getFackClient(self):
        for i in range(0, 20):
            print(str(i))
            self.btngroup = QtWidgets.QButtonGroup()
            self.status = QtWidgets.QPushButton()
            self.name = QtWidgets.QPushButton()

            self.btngroup.addButton(self.status)
            self.btngroup.addButton(self.name)

            self.operate = OperateForm()
            self.ClientTable.setItem(i,1 ,QtWidgets.QTableWidgetItem("客户端：139"))
            self.ClientTable.setItem(i, 2, QtWidgets.QTableWidgetItem("地址：192.168.19.143"))
            self.ClientTable.setItem(i, 3, QtWidgets.QTableWidgetItem("基础客户端"))
            self.ClientTable.setCellWidget(i, 4, self.operate)

    def initSql(self):
        cnx = mysql.connector.connect(user='zvc', password='qwer1234',host='127.0.0.1', database='client')
        cnx.close()

class VersionForm(QtWidgets.QWidget, Ui_VersionForm):
    def __init__(self):
        super(VersionForm, self).__init__()
        self.setupUi(self)

class RulesForm(QtWidgets.QWidget, Ui_RulesForm):
    def __init__(self):
        super(RulesForm, self).__init__()
        self.setupUi(self)


class CProcessBar(QtWidgets.QWidget):

    def init(self):
        self.progressBar = QtWidgets.QProgressBar()
        self.progressBar.setGeometry(QtCore.QRect(250, 200, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

    def timeEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            self.progressBar.hide()
            return
        self.step = self.step + 1
        self.progressBar.setValue(self.step)


