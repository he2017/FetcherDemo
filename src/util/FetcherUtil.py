# -*- coding: utf-8 -*-
# 第一行加这个后，就可以加中文注释了
'''
Created on 2017年5月21日

@author: tony
'''
import httplib
import urllib
import urlparse
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

'''
抓取网页
'''
def fetchHtml(url):
    page = urllib.urlopen(url) #打开一个链接
    html = page.read() #读取数据
    return html #返回html内容

'''
抓取微博
'''
def fetchWeibo(url, cookie=''):
    ret = urlparse.urlparse(url)    # Parse input URL
    conn = httplib.HTTPConnection(ret.netloc)
    conn.request(method='GET', url=url , headers={'Cookie': cookie})
    return conn.getresponse().read()
