# -*- coding: utf-8 -*-
# 第一行加这个后，就可以加中文注释了
'''
Created on 2017年5月21日

@author: tony
'''
from util import CommonUtil
from util import MysqlUtil
from util import FetcherUtil

if __name__ == '__main__':
    #1. 第一步一个url变量
    url = 'https://www.douban.com/'
    #2. 第二步抓取网页内容
    html = FetcherUtil.fetchHtml(url) 
    #3. 将网页内容存储到DB
    urlSum = CommonUtil.getUrlSum(url)#将url转成固定长度的md5字符串
    result = MysqlUtil.saveHtml(urlSum, url, html)
    if result:
        print '保存网页成功'
    else:
        print '保存网页失败'
    html = MysqlUtil.getHtml(urlSum)
    if(html):
        print html.decode("utf-8")
    