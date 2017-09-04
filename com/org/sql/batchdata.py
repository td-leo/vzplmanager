import mysql
from datetime import date, datetime

from com.org.sql.database import Init_Data

class Batch_Data():
    def insertRecord(self, cursor):
        add_client = ("INSERT INTO record "
                        "(body, partment, eventtype, step,create_time) "
                        "VALUES ( %s, %s, %s, %s, %s)")

        data_client1 = ('xx逃跑事件', 'A区B分部派出所', '处理人员逃跑事件',
                        '当接到xx逃跑后，当日值班大队领导立即向指挥长，副指挥报告',
                        datetime(2016, 3, 18,1,2,34))
        data_client2 = ('xx逃跑事件', 'A区B分部派出所', '处理人员逃跑事件',
                        '现场组织人员沿逃跑线路追寻，其他人员分为两队火速赶往火车站，汽车站，高速公路收费站站点堵截',
                        datetime(2016, 3, 18,1,2,44))
        data_client3 = ('xx逃跑事件', 'A区B分部派出所', '处理人员逃跑事件',
                        '现场警戒组维持好现场顺序，了解逃跑人员情况，做好其他人思想教育工作，随时做好现场支持准备',
                        datetime(2016, 3, 18,1,2,54))


        cursor.execute(add_client, data_client1)
        cursor.execute(add_client, data_client2)
        cursor.execute(add_client, data_client3)


    def insertUser(self, cursor):
        add_user = ("INSERT INTO user "
                        "(username, account,partment,create_time) "
                        "VALUES (%s, %s, %s, %s)")

        data_user1 = ('test1', '超級管理員', '偵查科', datetime(2017,3, 21, 12, 56, 28))
        data_user2= ('test2', '管理員', '資料室', datetime(2017, 3, 21, 12, 56, 28))
        data_user3 = ('test3', '管理员', '后勤处', datetime(2017, 3, 21, 12, 56, 28))
        cursor.execute(add_user, data_user1)
        cursor.execute(add_user, data_user2)
        cursor.execute(add_user, data_user3)

    def insertpermission(self, cursor):
        add_user = ("INSERT INTO permission "
                        "(account, value) "
                        "VALUES (%s, %s)")

        data_user = ('超級管理員', '9999')
        data_user1 = ('管理員', '9000')

        cursor.execute(add_user, data_user)
        cursor.execute(add_user, data_user1)

    def init(self):
        cnx = mysql.connector.connect(user='root', password='qwer1234',
                              host='127.0.0.1', database='vzplmanager')
        cursor = cnx.cursor()

        self.insertRecord(cursor)
        self.insertUser(cursor)
        self.insertpermission(cursor)


        cnx.commit()
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    sql = Init_Data()
    sql.delete()
    sql.init()

    batch = Batch_Data()
    batch.init()
