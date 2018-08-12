# -*- coding: utf-8 -*-
# @Time    : 2018/8/12 14:51
# @Author  : zhangdi
# @FileName: shorturl.py
# @Software: PyCharm

"""
使用哈希算法生成key
"""

import hashlib
import const


class GenerateShortUrl(object):

    def get_md5(self, s):
        if len(s) == 0:
            return const.err_url_empty
        m = hashlib.md5()
        m.update(s)
        return m.hexdigest()

    def get_hash_key(self, long_url):
        """
        md5编码
        :param long_url:
        :return:
        """
        key = 'yourkey'
        hkeys = []
        urlhex = self.get_md5(key + long_url)
        for i in xrange(0, 4):
            n = int(urlhex[i * 8:(i + 1) * 8], 16)
            v = []
            e = 0
            for j in xrange(0, 5):
                x = 0x0000003D & n
                e |= ((0x00000002 & n) >> 1) << j
                v.insert(0, const.code_map[x])
                n = n >> 6
            e |= n << 5
            v.insert(0, const.code_map[e & 0x0000003D])
            hkeys.append(''.join(v))
        return hkeys
