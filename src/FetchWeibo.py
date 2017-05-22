# -*- coding: utf-8 -*-
# 第一行加这个后，就可以加中文注释了
'''
Created on 2017年5月21日

@author: tony
'''
from util import CommonUtil, FileUtil, FetcherUtil, MysqlUtil, HtmlExtract

if __name__ == '__main__':
    #1. 初始化变量
    url = 'http://s.weibo.com/weibo/%25E4%25BA%25AC%25E4%25B8%259C&b=1&page=1'
    cookie_str = 'SINAGLOBAL=2204125497955.829.1485329104913; wvr=6; SSOLoginState=1495468461; SCF=Ah6FvK5u7EHN9tYhyolKNjlJFG4syHY2CW9__5jrTG_wHyAoTL3gmf4f7mF53Ds5memByMPu2qKaFqGwTTzI2_A.; SUB=_2A250J3n1DeThGeNI6VQV-SbJzD2IHXVXVew9rDV8PUNbmtANLUOjkW9oz_7t0I2S-F0znDPC68thLLDiRA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFv6clAKgcmksgpb_WU.yRA5JpX5KMhUgL.Fo-ceoqX1KnfS022dJLoI7LQ9Hv3Ug4N9g.t; SUHB=0YhB01PSEu8a54; ALF=1527004461; SWB=usrmdinst_12; _s_tentry=login.sina.com.cn; Apache=6693871708121.15.1495468465585; ULV=1495468465626:54:11:2:6693871708121.15.1495468465585:1495344744894; UOR=,,login.sina.com.cn; WBStorage=02e13baf68409715|undefined'
    #2. 首先从Mysql中获取快照
    urlSum = CommonUtil.getUrlSum(url)
    html = MysqlUtil.getHtml(urlSum)
    #3. 如果Mysql没有快照，则实时的从网上抓取快照
    if not html:
        html = FetcherUtil.fetchWeibo(url, cookie_str)
        result = MysqlUtil.saveHtml(urlSum, url, html) #抓取王快照后存储本地Mysql中
        if result:
            print '保存微博快照成功'
        else:
            print '保存微博快照失败'
    
    FileUtil.writeLine("weibo.html", html) #保存快照到临时文件中
    #4. 从html快照中提取结构化的微博内容
    weiboDatas = HtmlExtract.extractWeiboContent(html) 
    #5. 输入提取到的微博结构化内容
    for weiboData in weiboDatas:
        print '作者:', weiboData['author']
        print '发布时间:', weiboData['pubTime']
        print '内容:', weiboData['text']
        print ''
    print '找到', len(weiboDatas), '条微博'
    #6. 存储到Mysql中