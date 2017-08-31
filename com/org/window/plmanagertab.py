# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\workspace\vzplmanager\com\org\ui\plmanagertab.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

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
        self.treeWidget.setGeometry(QtCore.QRect(20, 60, 371, 341))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.graphicsView = QtWidgets.QGraphicsView(self.tab)
        self.graphicsView.setGeometry(QtCore.QRect(20, 10, 111, 31))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(150, 20, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(230, 20, 131, 16))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(230, 30, 111, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(300, 370, 51, 23))
        self.pushButton.setObjectName("pushButton")
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
        self.tabWidget.addTab(self.tab_4, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.treeWidget.headerItem().setText(0, _translate("Form", "事件类型"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Form", "处理人员逃跑事件"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("Form", "一级"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("Form", "处理人员械斗,群殴事件"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("Form", "一级"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("Form", "处理人员所内乱事件"))
        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("Form", "一级"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Form", "当前单位："))
        self.label_2.setText(_translate("Form", "xxx"))
        self.pushButton.setText(_translate("Form", "启动"))
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


    def initTab2(self):
        tab2 = [[True,"当接到xx逃跑后，当日值班大队领导立即向指挥长，副指挥报告","8-13 12:12", True],
                [True, "现场组织人员沿逃跑线路追寻，其他人员分为两队火速赶往火车站，汽车站，高速公路收费站站点堵截", "8-13 12:14", True],
                [True, "现场警戒组维持好现场顺序，了解逃跑人员情况，做好其他人思想教育工作，随时做好现场支持准备", "8-13 14:52", True]]

        for i in range(len(tab2)):
            self.tableWidget.setCellWidget(i, 0, QtWidgets.QCheckBox("状态") )
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(tab2[i][1]))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(tab2[i][2]))
            self.tableWidget.setCellWidget(i, 3, QtWidgets.QPushButton("完成"))

    def initTab3(self):
        tab3 = [[True,"当接到xx逃跑后，当日值班大队领导立即向指挥长，副指挥报告","8-13 12:12", True],
                [True, "现场组织人员沿逃跑线路追寻，其他人员分为两队火速赶往火车站，汽车站，高速公路收费站站点堵截", "8-13 12:14", True],
                [True, "现场警戒组维持好现场顺序，了解逃跑人员情况，做好其他人思想教育工作，随时做好现场支持准备", "8-13 14:52", True]]

        for i in range(len(tab3)):
            self.tableWidget_2.setCellWidget(i, 0, QtWidgets.QCheckBox("状态") )
            self.tableWidget_2.setItem(i, 1, QtWidgets.QTableWidgetItem(tab3[i][1]))
            self.tableWidget_2.setItem(i, 2, QtWidgets.QTableWidgetItem(tab3[i][2]))
            self.tableWidget_2.setCellWidget(i, 3, PlOperateForm())
            self.tableWidget_2.setCellWidget(i, 4, QtWidgets.QPushButton("完成"))


    def onItemChange(self, item, text):
        pass

class PlOperateForm(QtWidgets.QWidget, Ui_PlOperateForm):
    def __init__(self):
        super(PlOperateForm, self).__init__()
        self.setupUi(self)
