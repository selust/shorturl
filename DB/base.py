# -*- coding: utf-8 -*-
# @Time    : 2018/8/12 11:17
# @Author  : zhangdi
# @FileName: base.py
# @Software: PyCharm

import MySQLdb


class MysqlOperationBase(object):

    def __init__(self):
        #   打开数据库连接
        try:
            self.session = MySQLdb.connect("localhost", "root", "root", "shorturl", charset='utf8')
        except Exception as e:
            print e
            return
        #   检查表是否已经创建，若未创建则创建表
        self.cursor = self.session.cursor()
        try:
            sql = '''CREATE TABLE SHORTRURL IF NOT EXISTS SHORTRURL (
                     LURL CHAR(255) NOT NULL,
                     SURL CHAR(255) NOT NULL,
                     NUM INT )'''
            self.cursor.execute(sql)
        except Exception as e:
            print e
            return


    def __del__(self):
        #  断开数据库连接
        try:
            self.session.close()
        except Exception as e:
            print e
            return

    def insert(self, data):
        """
        插入时为第一次，则置访问计数为0
        :param data:
        :return:
        """
        sql = """INSERT INTO SHORTRURL(LURL,
                 SURL, NUM)
                 VALUES (\'{}\',\'{}\',\'{}\',)""".format(data['lurl'], data['surl'], 0)

        try:
            self.cursor.execute(sql)
            self.session.commit()
        except:
            self.session.rollback()
            return
        return 0

    def update(self, data):
        """
        当有用户点击访问某个链接时，访问数+1
        :param data:
        :return:
        """
        sql = "UPDATE SHORTURL SET NUM = NUM + 1 WHERE LURL = {}".format(data['lurl'])
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.session.commit()
        except:
            # 发生错误时回滚
            self.session.rollback()
            return
        return 0

    def query(self, key):
        """
        输入某个链接时，返回访问次数
        :param data:
        :return:
        """
        sql = "SELECT * FROM SHORTURL WHERE LURL = {}".format(key)
        # 执行SQL语句
        self.cursor.execute(sql)
        # 获取记录
        results = self.cursor.fetchall()
        return results











