# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 0:48
# @Author  : zhangdi
# @FileName: http.py
# @Software: PyCharm

import httplib
import const

def getweb(url):
    '''
    输入返回网址获取到的响应内容
    :return:
    '''

    http_client=httplib.HTTPConnection(url, 80, timeout=20)
    http_client.request('GET', '/')
    r = http_client.getresponse()

    if r.reason != 'OK':
        return const.get_web_fail
    else:
        return r.read()
