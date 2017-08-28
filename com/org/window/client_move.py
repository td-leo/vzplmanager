# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_move.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 475)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 40, 771, 331))
        self.textBrowser.setObjectName("textBrowser")
        self.button_cancle = QtWidgets.QPushButton(self.centralwidget)
        self.button_cancle.setGeometry(QtCore.QRect(740, 380, 60, 30))
        self.button_cancle.setObjectName("button_cancle")
        self.button_ok = QtWidgets.QPushButton(self.centralwidget)
        self.button_ok.setGeometry(QtCore.QRect(660, 380, 60, 30))
        self.button_ok.setObjectName("button_ok")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.button_ok.clicked.connect(self.slofNewWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def slofNewWindow(self):
        print('aaa')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_cancle.setText(_translate("MainWindow", "取消"))
        self.button_ok.setText(_translate("MainWindow", "确定"))

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    entry=Ui_MainWindow()
    entry.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())