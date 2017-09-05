# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

from com.org.window.plmanagertab import Ui_PlManagerForm
from com.org.window.plrecord import Ui_PlRecordForm
from com.org.window.plrecorder import Ui_RecorderForm
from com.org.window.plsystem import Ui_SystemForm


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(964, 540)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 961, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.mainlayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.mainlayout.setContentsMargins(0, 0, 0, 0)
        self.mainlayout.setObjectName("mainlayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionpl = QtWidgets.QAction(QIcon('img/plmanger.png'), "接警管理", MainWindow)
        self.actionpl.setObjectName("plmanager")

        self.actionrecord = QtWidgets.QAction(QIcon('img/plrecord.png'), "接警记录", MainWindow)
        self.actionrecord.setObjectName("plrecord")

        self.actioncase = QtWidgets.QAction(QIcon('img/plcase.png'), "数字预案", MainWindow)
        self.actioncase.setObjectName("plcase")

        self.actionpractice = QtWidgets.QAction(QIcon('img/plpractice.png'), "应急演练", MainWindow)
        self.actionpractice.setObjectName("plpractice")

        self.actionquery = QtWidgets.QAction(QIcon('img/plquery.png'), "录音查询", MainWindow)
        self.actionquery.setObjectName("plquery")

        self.actionsystem = QtWidgets.QAction(QIcon('img/plsettings.png'), "系统管理", MainWindow)
        self.actionsystem.setObjectName("plsettings")

        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.addAction(self.actionpl)
        self.toolBar.addAction(self.actionrecord)
        self.toolBar.addAction(self.actioncase)
        self.toolBar.addAction(self.actionpractice)
        self.toolBar.addAction(self.actionquery)
        self.toolBar.addAction(self.actionsystem)

        self.actionpl.triggered.connect(self.showPl)
        self.actionrecord.triggered.connect(self.showRecord)
        self.actioncase.triggered.connect(self.showCase)
        self.actionpractice.triggered.connect(self.showPractice)
        self.actionquery.triggered.connect(self.showQuery)
        self.actionsystem.triggered.connect(self.showSystem)


        self.toolBar.setMovable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.plmanager = PlManagerForm()
        self.plrecord = PlRecordForm()
        self.plsystem = PlSystemForm()
        self.recorder = RecorderForm()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


    def clearWidget(self):
        self.mainlayout.removeWidget(self.plmanager)
        self.plmanager.hide()

        self.mainlayout.removeWidget(self.plrecord)
        self.plrecord.hide()

        self.mainlayout.removeWidget(self.plsystem)
        self.plsystem.hide()

        self.mainlayout.removeWidget(self.recorder)
        self.recorder.hide()

        pass

    def showPl(self):
        self.clearWidget()
        self.mainlayout.addWidget(self.plmanager)
        self.plmanager.show()

    def showRecord(self):
        self.clearWidget()
        self.mainlayout.addWidget(self.plrecord)
        self.plrecord.show()

    def showCase(self):
        pass

    def showPractice(self):
        pass

    def showQuery(self):
        self.clearWidget()
        self.mainlayout.addWidget(self.recorder)
        self.recorder.show()


    def showSystem(self):
        self.clearWidget()
        self.mainlayout.addWidget(self.plsystem)
        self.plsystem.show()



class PlRecordForm(QtWidgets.QWidget, Ui_PlRecordForm):
    def __init__(self):
        super(PlRecordForm, self).__init__()
        self.setupUi(self)

class RecorderForm(QtWidgets.QWidget, Ui_RecorderForm):
    def __init__(self):
        super(RecorderForm, self).__init__()
        self.setupUi(self)

class PlManagerForm(QtWidgets.QWidget, Ui_PlManagerForm):
    def __init__(self):
        super(PlManagerForm, self).__init__()
        self.setupUi(self)

class PlSystemForm(QtWidgets.QWidget, Ui_SystemForm):
    def __init__(self):
        super(PlSystemForm, self).__init__()
        self.setupUi(self)

if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())