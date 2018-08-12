# -*- coding: utf-8 -*-
# @Time    : 2018/8/12 23:40
# @Author  : zhangdi
# @FileName: http.py
# @Software: PyCharm

from Tkinter import *
import tkMessageBox
from shorturl.shorturl import *
from DB.base import *
from http import getweb


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createwidgets()
        self.createwidgets2()
        self.createwidgets3()

    def createwidgets(self):
        """
        输入长链接获取短链接，并保存至数据库
        :return:
        """
        self.urlInput = Entry(self)
        self.urlInput.pack()
        self.alertButton = Button(self, text='获取短链接', command=self.show_shorturl)
        self.alertButton.pack()

    def createwidgets2(self):
        """
        输入某个网址，获取访问计数
        :return:
        """
        self.urlInput = Entry(self)
        self.urlInput.pack()
        self.alertButton = Button(self, text='获取访问计数', command=self.get_num)
        self.alertButton.pack()

    def createwidgets3(self):
        """
        输入短链接，访问某个网站
        :return:
        """
        self.urlInput = Entry(self)
        self.urlInput.pack()
        self.alertButton = Button(self, text='请输入短链接，获取网站内容', command=self.showshorturl)
        self.alertButton.pack()

    def show_shorturl(self):
        """
        生成短链接，并保存至数据库
        :return:
        """
        #  生成短链接，取第一个
        lurl = self.urlInput.get()
        g = GenerateShortUrl()
        surl = g.get_hash_key(lurl)[0]

        # 查询数据库中是否存在该记录，若有则直接显示，若无则插入一条新的记录
        sqlop = MysqlOperationBase()
        result = sqlop.query(lurl)
        if len(result) == 0:
            pass
        else:
            data = {'LURL': lurl, 'SURL': surl}
            sqlop.insert(data)
        tkMessageBox.showinfo('Message', '%s' % surl)

    def get_num(self):
        """
        查询数据库，获取访问计数
        :return:
        """
        lurl = self.urlInput.get()
        sqlop = MysqlOperationBase()
        result = sqlop.query(lurl)
        if len(result) == 0:
            tkMessageBox.showinfo('Message', '无此链接记录')
        else:
            tkMessageBox.showinfo('Message', '%s' % result[2])

    def get_web_text(self):
        """
        查询数据库，获取短链接对应的网址，并获取其内容
        :return:
        """
        surl = self.urlInput.get()
        sqlop = MysqlOperationBase()
        result = sqlop.query(surl)
        if len(result) == 0:
            tkMessageBox.showinfo('Message', '无此链接记录')
        else:
            txt = getweb(result[1])
            tkMessageBox.showinfo('Message', '%s' % txt)


app = Application()
# 设置窗口标题:
app.master.title('短链接服务窗口')
# 主消息循环:
app.mainloop()
