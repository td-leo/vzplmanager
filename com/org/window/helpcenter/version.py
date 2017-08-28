# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'version.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VersionForm(object):
    def setupUi(self, VersionForm):
        VersionForm.setObjectName("VersionForm")
        VersionForm.resize(728, 448)
        self.label = QtWidgets.QLabel(VersionForm)
        self.label.setGeometry(QtCore.QRect(60, 60, 171, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(VersionForm)
        self.label_2.setGeometry(QtCore.QRect(60, 120, 171, 31))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(VersionForm)
        QtCore.QMetaObject.connectSlotsByName(VersionForm)

    def retranslateUi(self, VersionForm):
        _translate = QtCore.QCoreApplication.translate
        VersionForm.setWindowTitle(_translate("VersionForm", "Form"))
        self.label.setText(_translate("VersionForm", "您使用的软件版本是：V3.1.2"))
        self.label_2.setText(_translate("VersionForm", "感谢对云系统的支持！"))

