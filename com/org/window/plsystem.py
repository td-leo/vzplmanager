# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\workspace\vzplmanager\com\org\ui\plsystem.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from com.org.window.pladdpermission import Ui_AddPermissionMainWindow
from com.org.window.pladduser import Ui_AddUserMainWindow


class Ui_SystemForm(object):
    def setupUi(self, SystemForm):
        SystemForm.setObjectName("SystemForm")
        SystemForm.resize(960, 490)
        self.tabWidget = QtWidgets.QTabWidget(SystemForm)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 951, 501))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 10, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 10, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 10, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 931, 391))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
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
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 80, 931, 361))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(190, 10, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton_6.setAutoRepeatDelay(295)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(280, 10, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(100, 10, 75, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(590, 450, 101, 16))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton_17 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_17.setGeometry(QtCore.QRect(190, 30, 75, 23))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_18.setGeometry(QtCore.QRect(100, 30, 75, 23))
        self.pushButton_18.setObjectName("pushButton_18")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_5.setGeometry(QtCore.QRect(10, 100, 931, 361))
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(4)
        self.tableWidget_5.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, item)
        self.pushButton_19 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_19.setGeometry(QtCore.QRect(10, 30, 75, 23))
        self.pushButton_19.setAutoRepeatDelay(295)
        self.pushButton_19.setObjectName("pushButton_19")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.label_7.setObjectName("label_7")
        self.pushButton_20 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_20.setGeometry(QtCore.QRect(280, 30, 75, 23))
        self.pushButton_20.setObjectName("pushButton_20")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(SystemForm)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(SystemForm)

    def retranslateUi(self, SystemForm):
        _translate = QtCore.QCoreApplication.translate
        SystemForm.setWindowTitle(_translate("SystemForm", "Form"))
        self.pushButton.setText(_translate("SystemForm", "浏览"))
        self.pushButton_2.setText(_translate("SystemForm", "添加"))
        self.pushButton_3.setText(_translate("SystemForm", "修改"))
        self.pushButton_4.setText(_translate("SystemForm", "删除"))
        self.label.setText(_translate("SystemForm", "【查询结果】"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SystemForm", "席号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SystemForm", "状态"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("SystemForm", "权限编号"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("SystemForm", "权限名称"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("SystemForm", "备注"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("SystemForm", "权限管理"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("SystemForm", "状态"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("SystemForm", "账号"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("SystemForm", "修改名称"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("SystemForm", "用户名称"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("SystemForm", "部门"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("SystemForm", "备注"))
        self.label_2.setText(_translate("SystemForm", "【查询结果】"))
        self.pushButton_5.setText(_translate("SystemForm", "修改"))
        self.pushButton_6.setText(_translate("SystemForm", "浏览"))
        self.pushButton_7.setText(_translate("SystemForm", "删除"))
        self.pushButton_8.setText(_translate("SystemForm", "添加"))
        self.label_3.setText(_translate("SystemForm", "【共 20 条记录】"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("SystemForm", "用户管理"))
        self.pushButton_17.setText(_translate("SystemForm", "修改"))
        self.pushButton_18.setText(_translate("SystemForm", "添加"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("SystemForm", "部门"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("SystemForm", "人数"))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("SystemForm", "预备人员"))
        item = self.tableWidget_5.horizontalHeaderItem(3)
        item.setText(_translate("SystemForm", "备注"))
        self.pushButton_19.setText(_translate("SystemForm", "浏览"))
        self.label_7.setText(_translate("SystemForm", "【查询结果】"))
        self.pushButton_20.setText(_translate("SystemForm", "删除"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("SystemForm", "部门管理"))

        self.initSlot()

    def initSlot(self):
        self.pushButton_19.clicked.connect(self.queryPart)
        self.pushButton_6.clicked.connect(self.queryUser)
        self.pushButton.clicked.connect(self.queryPermission)

        self.pushButton_2.clicked.connect(self.addPermission)
        self.pushButton_3.clicked.connect(self.modifyPermission)
        self.pushButton_4.clicked.connect(self.deletePermission)

        self.pushButton_8.clicked.connect(self.addUser)
        self.pushButton_5.clicked.connect(self.modifyUser)
        self.pushButton_7.clicked.connect(self.deleteUser)

        self.pushButton_17.clicked.connect(self.modifyPart)
        self.pushButton_20.clicked.connect(self.deletePart)



    def queryPermission(self):
        permissions = [["001", "确认", "9999","超级管理员", ""]]
        self.tableWidget.setRowCount(10)
        for per in range(len(permissions)):
            for i in range(len(permissions[per])):
                self.tableWidget.setItem(per, i, QtWidgets.QTableWidgetItem(permissions[per][i]))

    def queryUser(self):
        users = [["确认", "test", "2017-08-29 14:20:13", "test", "xxx", "P"],
                 ["确认", "admin", "2015-08-09 10:13:43", "超级管理员", "xxx", "P"]]
        self.tableWidget_2.setRowCount(10)
        for user in range(len(users)):
            for i in range(len(users[user])):
                self.tableWidget_2.setItem(user, i, QtWidgets.QTableWidgetItem(users[user][i]))


    def queryPart(self):
        pass

    def addPermission(self):
        self.mainwindow = QtWidgets.QMainWindow()
        self.new_permission = Ui_AddPermissionMainWindow()
        self.new_permission.setupUi(self.mainwindow)
        self.mainwindow.show()

    def addUser(self):
        self.mainwindow = QtWidgets.QMainWindow()
        self.new_user = Ui_AddUserMainWindow()
        self.new_user.setupUi(self.mainwindow)
        self.mainwindow.show()

    def modifyPermission(self):
        pass

    def modifyPart(self):
        pass

    def modifyUser(self):
        pass

    def deletePermission(self):
        pass

    def deletePart(self):
        pass

    def deleteUser(self):
        pass

