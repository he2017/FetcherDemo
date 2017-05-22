# -*- coding: utf-8 -*-
# 第一行加这个后，就可以加中文注释了
'''
Created on 2017年5月21日

@author: tony
'''
import urllib

'''
抓取网页测试
'''
def fetchHtml(url):
    page = urllib.urlopen(url) #打开一个链接
    html = page.read() #读取数据
    return html #返回html内容