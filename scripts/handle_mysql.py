# ======================
# -*- coding: utf-8 -*-
# @author:LiZhuo
# @time  :2020/10/12 14:18
# @email :358840393@qq.com
# 今天的你要比昨天的你更优秀！
# ======================
import pymysql
import random
from scripts.handle_config import do_config
import sys
sys.path.append("..")
class HandleMysql:
    def __init__(self):
        self.conn = pymysql.connect(host = "192.168.10.65",
                                    user = do_config.get_value("mysql","user"),
                                    password = do_config.get_value("mysql","password"),
                                    port = do_config.get_int("mysql","port"),
                                    database = do_config.get_value("mysql","database"),
                                    charset = "utf8",
                                    cursorclass = pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()

    def get_value(self,sql,args=None,is_more=False):
        self.cursor.execute(sql,args=args)
        self.conn.commit()
        if is_more:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()
    def close(self):
        self.cursor.close()
        self.conn.close()
if __name__ == '__main__':
    do_mysql = HandleMysql()
    sql = "select * from dept;"
    value1 = do_mysql.get_value(sql)
    print(value1)