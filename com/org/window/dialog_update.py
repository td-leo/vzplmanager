# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_update.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from com.org.window.confirm_cdp import Ui_MainWindow

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 250)
        Dialog.setMinimumSize(QtCore.QSize(450, 250))
        Dialog.setMaximumSize(QtCore.QSize(450, 250))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget_3 = QtWidgets.QWidget(self.splitter)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setContentsMargins(20, -1, -1, 20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.radioButton = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_2.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_2.addWidget(self.radioButton_2)
        self.widget_4 = QtWidgets.QWidget(self.splitter)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_2.setMinimumSize(QtCore.QSize(40, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.widget_4)
        self.pushButton.setMinimumSize(QtCore.QSize(40, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "请选择恢复类型："))
        self.radioButton.setText(_translate("Dialog", "即时恢复（恢复当前最新数据）"))
        self.radioButton_2.setText(_translate("Dialog", "CDP恢复（恢复历史上某个时刻点的数据）"))
        self.pushButton_2.setText(_translate("Dialog", "确认"))
        self.pushButton.setText(_translate("Dialog", "取消"))

        self.pushButton.clicked.connect(self.onConfirm)

    def onConfirm(self):

        pass


