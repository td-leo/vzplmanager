# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\workspace\vzplmanager\com\org\ui\plrecorder.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!
import random

import mysql
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RecorderForm(object):
    def setupUi(self, RecorderForm):
        RecorderForm.setObjectName("RecorderForm")
        RecorderForm.resize(961, 487)
        self.tableWidget = QtWidgets.QTableWidget(RecorderForm)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 931, 401))
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
        self.label = QtWidgets.QLabel(RecorderForm)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 21))
        self.label.setObjectName("label")

        self.retranslateUi(RecorderForm)
        QtCore.QMetaObject.connectSlotsByName(RecorderForm)

    def retranslateUi(self, RecorderForm):
        _translate = QtCore.QCoreApplication.translate
        RecorderForm.setWindowTitle(_translate("RecorderForm", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("RecorderForm", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("RecorderForm", "案件"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("RecorderForm", "接警员"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("RecorderForm", "播放"))
        self.label.setText(_translate("RecorderForm", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#4a4a4a;\">查看接警录音：</span></p></body></html>"))

        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 550)
        self.initTab()

    def initTab(self):
        cnx = mysql.connector.connect(user='root', password='qwer1234',
                                      host='127.0.0.1', database='vzplmanager')
        self.cursor = cnx.cursor()
        query = (
        "select create_time, body, partment from record where id in (select min(id) from record group by body)")
        self.cursor.execute(query)

        self.num = 0

        for (create_time, body, partment) in self.cursor:
            people = random.choice(["李工","陈工","王工"])
            self.tableWidget.setItem(self.num, 0, QtWidgets.QTableWidgetItem(str(self.num+1)))
            self.tableWidget.setItem(self.num, 1, QtWidgets.QTableWidgetItem(body))
            self.tableWidget.setItem(self.num, 2, QtWidgets.QTableWidgetItem(people))
            pushButton = QtWidgets.QPushButton(self)
            pushButton.setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("../window/img/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            pushButton.setIcon(icon)
            pushButton.setIconSize(QtCore.QSize(23, 23))
            pushButton.setObjectName("pushButton")
            pushButton.clicked.connect(self.play)

            self.tableWidget.setCellWidget(self.num, 3, pushButton)

            self.num += 1

        cnx.commit()
        self.cursor.close()
        cnx.close()

    def play(self):
        print ("play")
        cap = cv2.VideoCapture("img/pl.mp4")

        while (1):
            # get a frame
            ret, frame = cap.read()
            # show a frame
            cv2.imshow("capture", frame)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

