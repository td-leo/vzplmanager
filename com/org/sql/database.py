from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode


class Init_Data():
    DB_NAME = 'cloud'
    TABLES = {}
    TABLES['client'] = (
        "CREATE TABLE `client` ("
        "  `client_no` int(11) NOT NULL AUTO_INCREMENT,"
        "  `client_name` varchar(128) NOT NULL,"
        "  `authonize` varchar(128) NOT NULL,"
        "  `package` varchar(128) NOT NULL,"
        "  `clouddir` varchar(128) NOT NULL,"
        "  `clientfiles` varchar(256) NOT NULL,"
        "  `backupname` varchar(256) NOT NULL,"
        "  `ipaddress` varchar(128) NOT NULL,"
        "  PRIMARY KEY (`client_no`)"
        ") ENGINE=InnoDB")

    TABLES['log'] = (
        "CREATE TABLE `log` ("
        "  `log_no` int(11) NOT NULL AUTO_INCREMENT,"
        "  `client_name` varchar(128) NOT NULL,"
        "  `restore_type` varchar(128) NOT NULL,"
        "  `operation` varchar(128) NOT NULL,"
        "  `client_files` varchar(256) NOT NULL,"
        "  `clouddir` varchar(256) NOT NULL,"
        "  `ipaddress` varchar(128) NOT NULL,"
        "  `restore_date` datetime NOT NULL,"
        "  PRIMARY KEY (`log_no`)"
        ") ENGINE=InnoDB")

    TABLES['backup_record'] = (
        "CREATE TABLE `backup_record` ("
        "  `record_no` int(11) NOT NULL AUTO_INCREMENT,"
        "  `client_name` varchar(128) NOT NULL,"
        "  `backup_name` varchar(128) NOT NULL,"
        "  `client_files` varchar(256) NOT NULL,"
        "  `clouddir` varchar(256) NOT NULL,"
        "  `ipaddress` varchar(128) NOT NULL,"
        "  PRIMARY KEY (`record_no`)"
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


