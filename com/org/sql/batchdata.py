import mysql
from datetime import date, datetime

from com.org.sql.database import Init_Data

class Batch_Data():
    def insertClient(self, cursor):
        add_client = ("INSERT INTO client "
                        "(client_name, authonize, package, clouddir, clientfiles, backupname, ipaddress) "
                        "VALUES ( %s, %s, %s, %s, %s, %s, %s)")

        data_client1 = ('149', 'CB894JH903J0890IU', '基础客户端套餐', 'cloud/34908765/', '', '','192.168.12.149')
        data_client2 = ('129', 'DB764JH9065490I3U', '基础客户端套餐', 'cloud/98750876/', '', '','192.168.12.129')
        data_client3 = ('111', 'H906DB7640I3J549U', '基础客户端套餐', 'cloud/08987576/', '', '','192.168.12.111')
        data_client4 = ('89', 'ASD898H9065490I3U', '基础客户端套餐', 'cloud/87698750/', '', '','192.168.62.89')
        data_client5 = ('80', '549064J6I3UASD898', '基础客户端套餐', 'cloud/50876987/', '', '','192.168.12.80')

        cursor.execute(add_client, data_client1)
        cursor.execute(add_client, data_client2)
        cursor.execute(add_client, data_client3)
        cursor.execute(add_client, data_client4)
        cursor.execute(add_client, data_client5)

    def insertLog(self, cursor):
        add_log = ("INSERT INTO log "
                        "(client_name, restore_type, client_files, operation,ipaddress, clouddir, restore_date) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s)")

        data_log = ('149', '即时恢复', 'C:/data/', 'backup', '192.168.12.149', 'cloud/34908765/', datetime(2016, 8, 18,12,34,11))
        data_log2 = ('149', 'CDP恢复', 'C:/files/readme.txt->C:/files/add.text', 'rename', '192.168.12.149','cloud/34908765/', datetime(2017, 1, 7,19,56,23))

        data_log4 = ('129', '即时恢复', 'C:/1290/', 'setarr', '192.168.12.129','cloud/98750876/', datetime(2016, 3, 18,1,2,34))
        data_log3 = ( '80', 'CDP恢复', 'C:/profiles/', 'backup', '192.168.12.80', 'cloud/50876987/', datetime(2016, 12, 7,3,15,19))

        cursor.execute(add_log, data_log)
        cursor.execute(add_log, data_log2)
        cursor.execute(add_log, data_log3)
        cursor.execute(add_log, data_log4)

    def insertUser(self, cursor):
        add_user = ("INSERT INTO account "
                        "(account, email, password, last_login, author) "
                        "VALUES (%s, %s, %s, %s, %s)")

        data_user = ('kaidylee', 'lidekai', 'kaidylee@vanzo.com', datetime(2017,3, 21, 12, 56, 28),  'gKwX1uNqzgHjXibOam0Hk/x096GeB36Sz')
        cursor.execute(add_user, data_user)


    def insertBackupRecord(self0, cursor):
        add_backup = ("INSERT INTO backup_record "
                        "(client_name, backup_name, client_files, clouddir,ipaddress) "
                        "VALUES (%s, %s, %s, %s, %s)")
        data_backup1 = ('149', 'data23', 'C:/data/;D:/files/', 'cloud/34908765/', '192.168.12.149')
        data_backup2 = ('129', 'backup1', 'C:/1290/', 'cloud/98750876/', '192.168.12.129')
        data_backup3 = ('129', 'backup2', 'C:/1790/', 'cloud/98750876/', '192.168.12.129')
        cursor.execute(add_backup, data_backup1)
        cursor.execute(add_backup, data_backup2)
        cursor.execute(add_backup, data_backup3)

    def init(self):
        cnx = mysql.connector.connect(user='root', password='qwer1234',
                              host='127.0.0.1', database='cloud')
        cursor = cnx.cursor()

        self.insertClient(cursor)
        self.insertLog(cursor)
        self.insertUser(cursor)
        self.insertBackupRecord(cursor)

        cnx.commit()
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    sql = Init_Data()
    sql.delete()
    sql.init()

    batch = Batch_Data()
    batch.init()
