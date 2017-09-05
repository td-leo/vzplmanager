from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode


class Init_Data():
    DB_NAME = 'vzplmanager'
    TABLES = {}
    TABLES['record'] = (
        "CREATE TABLE `record` ("
        "  `id` int(11) NOT NULL AUTO_INCREMENT,"
        "  `body` varchar(128) NOT NULL,"
        "  `partment` varchar(128) NOT NULL,"
        "  `eventtype` varchar(128) NOT NULL,"
        "  `step` varchar(128),"
        "  `create_time` datetime NOT NULL,"
        "  PRIMARY KEY (`id`)"
        ") ENGINE=InnoDB")

    TABLES['permission'] = (
        "CREATE TABLE `permission` ("
        "  `id` int(11) NOT NULL AUTO_INCREMENT,"
        "  `account` varchar(128) NOT NULL,"
        "  `value` varchar(128) NOT NULL,"
        "  PRIMARY KEY (`id`)"
        ") ENGINE=InnoDB")

    TABLES['user'] = (
        "CREATE TABLE `user` ("
        "  `id` int(11) NOT NULL AUTO_INCREMENT,"
        "  `username` varchar(128) NOT NULL,"
        "  `account` varchar(128) NOT NULL,"
        "  `partment` varchar(256) NOT NULL,"
        "  `create_time` datetime NOT NULL,"
        "  PRIMARY KEY (`id`)"
        ") ENGINE=InnoDB")

    TABLES['part'] = (
        "CREATE TABLE `part` ("
        "  `id` int(11) NOT NULL AUTO_INCREMENT,"
        "  `partment` varchar(128) NOT NULL,"
        "  `count` varchar(128) NOT NULL,"
        "  `extra_count` varchar(128) NOT NULL,"
        "  PRIMARY KEY (`id`)"
        ") ENGINE=InnoDB")

    TABLES['account'] = (
        "CREATE TABLE `account` ("
        "  `_id` int(11) NOT NULL AUTO_INCREMENT,"
        "  `account` varchar(128) NOT NULL,"
        "  `email` varchar(128) NOT NULL,"
        "  `password` varchar(128) NOT NULL,"
        "  `last_login` datetime NOT NULL,"
        "  `author` varchar(256) NOT NULL,"
        "  PRIMARY KEY (`_id`)"
        ") ENGINE=InnoDB")

    def create_database(self, cursor):
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(self.DB_NAME))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)


    def delete(self):
        cnx = mysql.connector.connect(user='root', password='qwer1234',
                              host='127.0.0.1')
        cursor = cnx.cursor()

        try:
            cursor.execute('drop database ' + self.DB_NAME + ';')
        except mysql.connector.Error as err:
            print(err)

        cnx.commit()
        cursor.close()
        cnx.close()


    def init(self):
        cnx = mysql.connector.connect(user='root', password='qwer1234',
                              host='127.0.0.1')
        cursor = cnx.cursor()
        try:
            cnx.database = self.DB_NAME
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.create_database(cursor)
                cnx.database = self.DB_NAME
            else:
                print(err)
                exit(1)

        for name, ddl in self.TABLES.items():
            try:
                print("Creating table {}: ".format(name), end='')
                cursor.execute(ddl)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")


