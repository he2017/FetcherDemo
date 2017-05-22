# -*- coding: utf-8 -*-
# 第一行加这个后，就可以加中文注释了
'''
Created on 2017年5月21日

@author: tony
'''
from util import FetcherUtil, MysqlUtil, HtmlExtract

'''
1. 从数据库中获取newsmeta信息
2. 根据newsmeta信息的url抓取对应的网页快照
3. 解析新闻内容
'''    
if __name__ == '__main__':
    #1. 从数据库中获取newsMeta
    newsMeta = MysqlUtil.getNewsMeta()
    htmls = {}
    for meta in newsMeta:
        print meta['id'], meta['url'], meta['urlSum'], meta['title']
        html = MysqlUtil.getHtml(meta['urlSum'])
        if not html:
            html = FetcherUtil.fetchHtml(meta['url']) #如果数据库中不存在html快照，则重新抓取
        detail = HtmlExtract.extractMeta(html)
        if detail:
            print "标题:", detail['title']
            print "作者:", detail['author']
            print "发布时间:", detail['pubTime']
            print "内容:", detail['content']
            if MysqlUtil.saveNewsContent(meta['url'], 
                                         meta['urlSum'], 
                                         detail['title'], 
                                         detail['author'],
                                         detail['pubTime'], 
                                         detail['content']):
                MysqlUtil.updateNewsMetaFetchedStatus(meta['urlSum']) #更新meta记录为已经抓取，防止重复抓取
        