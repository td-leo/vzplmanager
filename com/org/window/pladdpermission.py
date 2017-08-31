
# Form implementation generated from reading ui file 'D:\workspace\vzplmanager\com\org\ui\pladdpermission.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddPermissionMainWindow(object):
    def setupUi(self, AddPermissionMainWindow):
        AddPermissionMainWindow.setObjectName("AddPermissionMainWindow")
        AddPermissionMainWindow.resize(316, 378)
        self.centralwidget = QtWidgets.QWidget(AddPermissionMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(50, 60, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(50, 90, 71, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(50, 120, 71, 16))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(50, 150, 71, 16))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(50, 180, 71, 16))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(50, 210, 71, 16))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_10 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_10.setGeometry(QtCore.QRect(170, 120, 71, 16))
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_11.setGeometry(QtCore.QRect(170, 150, 71, 16))
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_12.setGeometry(QtCore.QRect(170, 90, 71, 16))
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_13.setGeometry(QtCore.QRect(170, 60, 71, 16))
        self.checkBox_13.setObjectName("checkBox_13")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(130, 330, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        AddPermissionMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AddPermissionMainWindow)
        self.statusbar.setObjectName("statusbar")
        AddPermissionMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddPermissionMainWindow)
        QtCore.QMetaObject.connectSlotsByName(AddPermissionMainWindow)

    def retranslateUi(self, AddPermissionMainWindow):
        _translate = QtCore.QCoreApplication.translate
        AddPermissionMainWindow.setWindowTitle(_translate("AddPermissionMainWindow", "MainWindow"))
        self.checkBox.setText(_translate("AddPermissionMainWindow", "接警管理"))
        self.checkBox_2.setText(_translate("AddPermissionMainWindow", "接警记录"))
        self.checkBox_3.setText(_translate("AddPermissionMainWindow", "数字预案"))
        self.checkBox_4.setText(_translate("AddPermissionMainWindow", "应急预案"))
        self.checkBox_5.setText(_translate("AddPermissionMainWindow", "录音查询"))
        self.checkBox_6.setText(_translate("AddPermissionMainWindow", "系统管理"))
        self.checkBox_10.setText(_translate("AddPermissionMainWindow", "消防管理"))
        self.checkBox_11.setText(_translate("AddPermissionMainWindow", "参数设置"))
        self.checkBox_12.setText(_translate("AddPermissionMainWindow", "实时监控"))
        self.checkBox_13.setText(_translate("AddPermissionMainWindow", "地图定位"))

