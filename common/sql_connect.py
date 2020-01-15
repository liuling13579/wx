# -*- coding:utf-8 -*-

import pymssql
import pymysql
from common import parm as P

#连接数据库-测试环境
class SQL_conn(object):
    def __init__(self):
        self.host = P.sql_server
        self.user = P.sql_user
        self.pwd = P.sql_pwd
        self.db = P.test_db
        self.port = 16033

    def sql_conn(self):
        #连接数据库
        self.conn = pymysql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,port=self.port)
        self.cursor = self.conn.cursor()     # 使用cursor()方法获取操作游标,获得python执行Mysql命令的方法

    def sql_change(self,sql):
        #操作数据（增删改）
        self.cursor.execute(sql)
        self.conn.commit()

    def sql_changes(self,sql,list_data):
        #批量操作数据（增删改）
        #sql = "insert into table(name,age) values(%s,%d)"
        #list_data = [("zhang",22),("wang",33)]
        self.cursor.execute(sql,list_data)
        self.conn.commit()

    def sql_search(self,sql):
        #查询
        #fetchall()则是接收全部的返回结果行 row就是在python中定义的一个变量，用来接收返回结果行的每行数据
        self.cursor.execute(sql)
        row = self.cursor.fetchall()
        List = []
        for i in row:
            List.append(i)
        return List

    def sql_close(self):
        #关闭连接
        self.cursor.close()
        self.conn.close()

    def sql_search1(self,sql,info):
        #查询
        #fetchall()则是接收全部的返回结果行 row就是在python中定义的一个变量，用来接收返回结果行的每行数据
        self.cursor.execute(sql,info)
        row = self.cursor.fetchall()
        List = []
        for i in row:
            List.append(i)
        return List

    def sql_search2(self,sql,info):
        S = SQL_conn()
        S.sql_conn()
        t = S.sql_search1(sql,info)
        print(t)
        # print(type(t))
        S.sql_close()
        return t


if __name__ == "__main__":
    # sql = "SELECT * FROM `account_protocol` a WHERE a.school_id in(11) AND a.account_type=1;"
    S = SQL_conn()
    course_id=140800423
    school_id=11
    # S.sql_conn()
    # t = S.sql_search(sql)
    # print(t)
    # print(type(t))
    # S.sql_close()
    sql="SELECT c.course_id,c.price FROM course c WHERE c.course_id=%s AND c.school_id=%s;"
    info = (course_id,school_id)
    try:
        t = S.sql_search2(sql,info)
        print(t[0][0])
    except:
        print ("Error: unable to fecth data")

