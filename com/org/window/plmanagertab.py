# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\workspace\vzplmanager\com\org\ui\plmanagertab.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!
import random

import mysql
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from com.org.window.ploperate import Ui_PlOperateForm


class Ui_PlManagerForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(925, 478)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(19, 10, 959, 461))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.treeWidget = QtWidgets.QTreeWidget(self.tab)
        self.treeWidget.setGeometry(QtCore.QRect(20, 70, 371, 351))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(190, 30, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(270, 30, 131, 16))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(270, 40, 111, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(300, 390, 51, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 61, 51))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../window/img/type.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(90, 20, 71, 31))
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 901, 421))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 10, 901, 421))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(10)
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
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(33, 20, 71, 20))
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit.setGeometry(QtCore.QRect(30, 50, 711, 121))
        self.textEdit.setObjectName("textEdit")
        self.label_6 = QtWidgets.QLabel(self.tab_4)
        self.label_6.setGeometry(QtCore.QRect(40, 200, 71, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(40, 250, 71, 20))
        self.label_7.setObjectName("label_7")
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(40, 290, 71, 20))
        self.label_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_4)
        self.label_16.setGeometry(QtCore.QRect(40, 330, 71, 20))
        self.label_16.setObjectName("label_16")
        self.line_4 = QtWidgets.QFrame(self.tab_4)
        self.line_4.setGeometry(QtCore.QRect(40, 220, 701, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_27 = QtWidgets.QLabel(self.tab_4)
        self.label_27.setGeometry(QtCore.QRect(410, 250, 101, 20))
        self.label_27.setObjectName("label_27")
        self.label_26 = QtWidgets.QLabel(self.tab_4)
        self.label_26.setGeometry(QtCore.QRect(150, 250, 101, 21))
        self.label_26.setObjectName("label_26")
        self.label_28 = QtWidgets.QLabel(self.tab_4)
        self.label_28.setGeometry(QtCore.QRect(150, 290, 101, 21))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.tab_4)
        self.label_29.setGeometry(QtCore.QRect(150, 330, 101, 21))
        self.label_29.setObjectName("label_29")
        self.label_32 = QtWidgets.QLabel(self.tab_4)
        self.label_32.setGeometry(QtCore.QRect(460, 290, 101, 21))
        self.label_32.setObjectName("label_32")
        self.tabWidget.addTab(self.tab_4, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.treeWidget.headerItem().setText(0, _translate("Form", "事件类型"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Form", "处理人员逃跑事件"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("Form", "B区xx所陈某逃跑事件"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("Form", "C片xx所李某逃跑事件"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("Form", "处理人员械斗,群殴事件"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("Form", "D区5街区打斗事件"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("Form", "A区3街区打斗事件"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("Form", "处理人员所内乱事件"))
        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("Form", "E区扰乱事件"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Form", "当前单位："))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#00aa00;\">A市X区指挥部门</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "启动"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">事件类型</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "应急事件"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "状态"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "详细信息"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "完成时间"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "操作"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "预案执行"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "状态"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "详细信息"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "完成时间"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "步骤修改"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Form", "操作"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "跟踪指挥"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">处理结果：</span></p></body></html>"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">案件在处理中</p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">组织架构</span></p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">指挥长：</span></p></body></html>"))
        self.label_15.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">执行指挥：</span></p></body></html>"))
        self.label_16.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">现场指挥：</span></p></body></html>"))
        self.label_27.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">指挥中心成员：</span></p></body></html>"))
        self.label_26.setText(_translate("Form", "李XX"))
        self.label_28.setText(_translate("Form", "陈XX"))
        self.label_29.setText(_translate("Form", "网XX"))
        self.label_32.setText(_translate("Form", "李XX， 王xx"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "处理结果"))

        self.treeWidget.itemClicked['QTreeWidgetItem*', 'int'].connect(self.onItemChange)
        self.pushButton.clicked.connect(self.start)

        self.tableWidget_2.setColumnWidth(1, 450)
        self.tableWidget.setColumnWidth(1, 550)

        self.initTab2()
        self.initTab3()

    def start(self):
        item = self.treeWidget.currentItem()
        item.setIcon(0, QIcon('img/running.png'))
        self.refresh()

    def refresh(self):
        self.initTab2()
        self.initTab3()
        self.initResult()


    def initResult(self):
        self.label_26.clear()
        self.label_28.clear()
        self.label_29.clear()
        self.label_32.clear()

        people = random.choice([["陈工","李某","王某","陈xx， 李xx， 王xxx"],
                                ["张工","颜某","吴某","吴xx， 李xx， 张xxx"],
                                ["李工","宋某","王某","高xx， 林xx， 王xxx"]])

        self.label_26.setText(people[0])
        self.label_28.setText(people[1])
        self.label_29.setText(people[2])
        self.label_32.setText(people[3])

    def initTab2(self):
        self.tableWidget.clear()
        cnx = mysql.connector.connect(user='root', password='qwer1234',
                              host='127.0.0.1', database='vzplmanager')
        self.cursor = cnx.cursor()
        query = ("select step, create_time from record where body='%s' order by create_time" %(self.event))
        self.cursor.execute(query)

        self.num = 0
        for (step, create_time) in self.cursor:
            self.tableWidget.setCellWidget(self.num, 0, QtWidgets.QCheckBox("状态") )
            self.tableWidget.setItem(self.num, 1, QtWidgets.QTableWidgetItem(step))
            self.tableWidget.setItem(self.num, 2, QtWidgets.QTableWidgetItem(str(create_time)))
            self.tableWidget.setCellWidget(self.num, 3, QtWidgets.QPushButton("完成"))
            self.num += 1

        cnx.commit()
        self.cursor.close()
        cnx.close()

    def clicktable2(self):
        print ("clicktable2")
    def initTab3(self):
        self.tableWidget_2.clear()
        self.tableWidget_2.clicked.connect(self.clicktable2)
        cnx = mysql.connector.connect(user='root', password='qwer1234',
                              host='127.0.0.1', database='vzplmanager')
        self.cursor = cnx.cursor()
        query = ("select body, partment, eventtype, step, create_time from record where body='%s' order by create_time" %(self.event))
        self.cursor.execute(query)

        self.num = 0
        for (body, partment, eventtype, step, create_time) in self.cursor:
            self.tableWidget_2.setCellWidget(self.num, 0, QtWidgets.QCheckBox("状态") )
            self.tableWidget_2.setItem(self.num, 1, QtWidgets.QTableWidgetItem(step))
            self.tableWidget.setItem(self.num, 2, QtWidgets.QTableWidgetItem(str(create_time)))
            operate = PlOperateForm()
            val = [body, partment, eventtype, step, create_time]
            operate.initdata(val)
            self.tableWidget_2.setCellWidget(self.num, 3, operate)
            self.tableWidget_2.setCellWidget(self.num, 4, QtWidgets.QPushButton("完成"))
            self.num += 1

        cnx.commit()
        self.cursor.close()
        cnx.close()

    def onItemChange(self, item, text):
        self.event = item.text(0)
        pass

class PlOperateForm(QtWidgets.QWidget, Ui_PlOperateForm):
    def __init__(self):
        super(PlOperateForm, self).__init__()
        self.setupUi(self)
