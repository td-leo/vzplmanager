# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progress.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtCore import QTimer


class Ui_ProgressForm(object):
    def setupUi(self, ProgressForm):
        ProgressForm.setObjectName("ProgressForm")
        ProgressForm.resize(80, 23)
        self.progressBar = QtWidgets.QProgressBar(ProgressForm)
        self.progressBar.setGeometry(QtCore.QRect(5, 0, 80, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.show()
        red = 'bb0c5c'
        style = """
                QProgressBar {
                    border: 2px solid grey;
                    border-radius: 5px;
                    text-align: center;
                }
                QProgressBar::chunk {
                    background-color: #%s;
                    width: 5px;
                }""" % red
        self.progressBar.setStyleSheet(style)
        self.retranslateUi(ProgressForm)
        QtCore.QMetaObject.connectSlotsByName(ProgressForm)
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.onTimeOut)
        self.step = 0


    def onStart(self):
        print("onStart timer")
        self.timer.start(100)

    def onStop(self):
        self.timer.stop()

    def onTimeOut(self):
        if self.step >=100:
            self.timer.stop()
            return
        self.step = self.step + 1
        self.progressBar.setValue(self.step)

    def retranslateUi(self, ProgressForm):
        _translate = QtCore.QCoreApplication.translate
        ProgressForm.setWindowTitle(_translate("ProgressForm", "Form"))


if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    entry=Ui_ProgressForm()
    entry.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())