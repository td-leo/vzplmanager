from PyQt5 import QtWidgets

from com.org.sql.batchdata import Batch_Data
from com.org.sql.database import Init_Data
from com.org.window.main import Ui_MainWindow

if __name__=="__main__":
    import sys

    sql = Init_Data()
    sql.delete()
    sql.init()

    batch = Batch_Data()
    batch.init()

    app=QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    entry=Ui_MainWindow()
    entry.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())