import mysql
from datetime import date, datetime

from com.org.sql.database import Init_Data

class Batch_Data():
    def insertRecord(self, cursor):
        add_client = ("INSERT INTO record "
                        "(body, partment, eventtype, step,create_time) "
                        "VALUES ( %s, %s, %s, %s, %s)")

        data_client1 = ('B区xx所陈某逃跑事件', 'B区xx所', '处理人员逃跑事件',
                        '当接到xx逃跑后，当日值班大队领导立即向指挥长，副指挥报告',
                        datetime(2017, 3, 18,1,2,34))
        data_client2 = ('B区xx所陈某逃跑事件', 'B区xx所', '处理人员逃跑事件',
                        '现场组织人员沿逃跑线路追寻，其他人员分为两队火速赶往火车站，汽车站，高速公路收费站站点堵截',
                        datetime(2017, 3, 18,1,2,44))
        data_client3 = ('B区xx所陈某逃跑事件', 'B区xx所', '处理人员逃跑事件',
                        '现场警戒组维持好现场顺序，了解逃跑人员情况，做好其他人思想教育工作，随时做好现场支持准备',
                        datetime(2017, 3, 18,1,2,54))

        data_client4 = ('C片xx所李某逃跑事件', 'C区xx所', '处理人员逃跑事件',
                        '当接到李某逃跑后，当日值班大队领导立即向指挥长，副指挥报告',
                        datetime(2017, 4, 22,1,2,34))

        data_client5 = ('D区5街区打斗事件', 'D区xx所', '处理人员械斗,群殴事件',
                        '当接到D街区打斗事件后，当日值班大队领导立即向指挥长，副指挥报告',
                        datetime(2017, 5, 8,1,2,34))

        data_client6 = ('A区3街区打斗事件', 'A区xx所', '处理人员械斗,群殴事件',
                        '当接到A区3街区逃跑后，当日值班大队领导立即向指挥长，副指挥报告',
                        datetime(2017, 6, 18, 1, 12, 3))

        data_client7 = ('E区扰乱事件', 'E区xx所', '处理人员所内乱事件',
                        '当接到E区扰乱事件后，当日值班大队领导立即向指挥长，副指挥报告',
                        datetime(2017, 5, 18, 8, 8, 3))




        cursor.execute(add_client, data_client1)
        cursor.execute(add_client, data_client2)
        cursor.execute(add_client, data_client3)
        cursor.execute(add_client, data_client4)
        cursor.execute(add_client, data_client5)
        cursor.execute(add_client, data_client6)
        cursor.execute(add_client, data_client7)


    def insertUser(self, cursor):
        add_user = ("INSERT INTO user "
                        "(username, account,partment,create_time) "
                        "VALUES (%s, %s, %s, %s)")

        data_user1 = ('test1', '超級管理員', '侦查科', datetime(2017,3, 21, 12, 56, 28))
        data_user2= ('test2', '管理員', '資料室', datetime(2017, 3, 21, 12, 56, 28))
        data_user3 = ('test3', '管理员', '后勤处', datetime(2017, 3, 21, 12, 56, 28))
        data_user4 = ('test4', '普通用户', '接警处', datetime(2017, 3, 21, 12, 56, 28))
        data_user5 = ('test5', '普通用户', '接警处', datetime(2017, 3, 21, 12, 56, 28))
        cursor.execute(add_user, data_user1)
        cursor.execute(add_user, data_user2)
        cursor.execute(add_user, data_user3)
        cursor.execute(add_user, data_user4)
        cursor.execute(add_user, data_user5)

    def insertpermission(self, cursor):
        add_user = ("INSERT INTO permission "
                        "(account, value) "
                        "VALUES (%s, %s)")

        data_user = ('超級管理員', '9999')
        data_user1 = ('管理員', '9000')
        data_user2 = ('普通用户', '8080')

        cursor.execute(add_user, data_user)
        cursor.execute(add_user, data_user1)
        cursor.execute(add_user, data_user2)

    def insertpart(self, cursor):
        add_user = ("INSERT INTO part "
                        "(partment, count, extra_count) "
                        "VALUES (%s, %s, %s)")

        data_user = ('接警处', '5', '1')
        data_user1 = ('后勤处','10', '0')
        data_user2 = ('侦查科', '15', '0')
        data_user3 = ('资料室', '2', '0')

        cursor.execute(add_user, data_user)
        cursor.execute(add_user, data_user1)
        cursor.execute(add_user, data_user2)
        cursor.execute(add_user, data_user3)

    def init(self):
        cnx = mysql.connector.connect(user='root', password='qwer1234',
                              host='127.0.0.1', database='vzplmanager')
        cursor = cnx.cursor()

        self.insertRecord(cursor)
        self.insertUser(cursor)
        self.insertpermission(cursor)
        self.insertpart(cursor)


        cnx.commit()
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    sql = Init_Data()
    sql.delete()
    sql.init()

    batch = Batch_Data()
    batch.init()
