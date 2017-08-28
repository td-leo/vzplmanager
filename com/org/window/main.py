# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!
from datetime import datetime

import mysql
from PyQt5 import QtCore, QtWidgets


from com.org.window.acount import Ui_AccountForm
from com.org.window.helpcenter.contact import Ui_ContactForm
from com.org.window.helpcenter.version import Ui_VersionForm

from com.org.window.log import Ui_LogForm
from com.org.window.query import Ui_QueryForm
from com.org.window.rules import Ui_RulesForm
from com.org.window.settings import Ui_SetingsForm


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(10, 40, 151, 451))
        self.treeWidget.setObjectName("treeWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(180, 40, 731, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.mainlayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.mainlayout.setContentsMargins(0, 0, 0, 0)
        self.mainlayout.setObjectName("mainlayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.treeWidget.itemClicked['QTreeWidgetItem*','int'].connect(self.onItemChange)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.account = AccountForm()
        self.settings = SettingsForm()
        self.tab =
        self.log = LogForm()
        self.query = QueryForm()
        self.contact = ContactForm()
        self.version = VersionForm()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "云系统"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.setColumnCount(1)
        for i in range(1):
            child = QtWidgets.QTreeWidgetItem(self.treeWidget)
            info = QtWidgets.QTreeWidgetItem(child)
            child.setText(0, _translate("MainWindow", "admin"))
            info.setText(0, _translate("MainWindow", "110032"))
            info.setText(1, _translate("MainWindow", "201"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)

    def showAccount(self):
        self.clearWidget()
        self.mainlayout.addWidget(self.account)
        self.account.show()

    def showSettings(self):
        self.clearWidget()
        self.mainlayout.addWidget(self.settings)
        self.settings.show()

    def showTab(self):
        self.clearWidget()
        self.mainlayout.addWidget(self.)
    def showLog(self):
        self.clearWidget()
        self.mainlayout.addWidget(self.log)
        self.log.show()

    def showContact(self):
        self.clearWidget()
        self.mainlayout.addWidget(self.contact)
        self.contact.show()

    def showVersion(self):
        self.clearWidget()
        self.mainlayout.addWidget(self.version)
        self.version.show()

    def showRules(self):
        pass

    def showQuery(self):
        self.clearWidget()
        self.mainlayout.addWidget(self.query)
        self.query.show()

    def clearWidget(self):
        self.mainlayout.removeWidget(self.account)
        self.mainlayout.removeWidget(self.settings)
        self.mainlayout.removeWidget(self.log)
        self.mainlayout.removeWidget(self.query)
        self.mainlayout.removeWidget(self.contact)
        self.mainlayout.removeWidget(self.version)
        self.account.hide()
        self.settings.hide()
        self.log.hide()
        self.query.hide()
        self.version.hide()
        self.contact.hide()

    def onItemChange(self, item, text):
        self.clearWidget()

        if item.text(0) == "admin":
            self.showSettings()
        elif item.text(0) == "日志":
            self.showLog()
        elif item.text(0) == "查询/恢复":
            self.showQuery()
        elif item.text(0) == "联系我们":
            self.showContact()
        elif item.text(0) == "软件版本":
            self.showVersion()
        elif item.text(0) == "信息":
            self.showAccount()

class AccountForm(QtWidgets.QWidget, Ui_AccountForm):
    def __init__(self):
        super(AccountForm, self).__init__()
        self.setupUi(self)
        self.initData()

    def initData(self):
        cnx = mysql.connector.connect(user='root', password='qwer1234',
                              host='127.0.0.1', database='cloud')
        cursor = cnx.cursor()
        query = ("select account, email, last_login, author from account")
        cursor.execute(query)
        for (account, email, last_login, author) in cursor:
            self.textEdit.setText(account)
            self.textEdit_2.setText(email)
            self.textEdit_3.setText(datetime.strftime(last_login, '%Y-%m-%d %H:%M:%S'))
            self.textEdit_4.setText(author)

        cursor.close()
        cnx.close()

class SettingsForm(QtWidgets.QWidget, Ui_SetingsForm):
    def __init__(self):
        super(SettingsForm, self).__init__()
        self.setupUi(self)

class SettingsForm(QtWidgets.QWidget, Ui_SetingsForm):
    def __init__(self):
        super(SettingsForm, self).__init__()
        self.setupUi(self)

class LogForm(QtWidgets.QWidget, Ui_LogForm):
    def __init__(self):
        super(LogForm, self).__init__()
        self.setupUi(self)

class QueryForm(QtWidgets.QWidget, Ui_QueryForm):
    def __init__(self):
        super(QueryForm, self).__init__()
        self.setupUi(self)

class VersionForm(QtWidgets.QWidget, Ui_VersionForm):
    def __init__(self):
        super(VersionForm, self).__init__()
        self.setupUi(self)

class ContactForm(QtWidgets.QWidget, Ui_ContactForm):
    def __init__(self):
        super(ContactForm, self).__init__()
        self.setupUi(self)


if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())