# -*- coding: utf-8 -*-
# 第一行加这个后，就可以加中文注释了
'''
Created on 2017年5月21日

@author: tony
''' 
from HTMLParser import HTMLParser
import re

'''    
提取链接，返回一个链接数组
'''
def extractLink(html):
    reg = r'<a(.*?)href="(.*?)"(.*?)>(.*?)</a>'
    groups = re.findall(reg, html, re.S|re.M)
    links = []
    for group in groups:
        link = group[1] #找到匹配的链接group
        if(link.strip() != ''): #链接不为空的时候再返回
            links.append(link)
    return links

'''
提取豆瓣首页里面的新闻链接地址和标题
'''
def extractDoubanNews(html):
    reg = r'class="notes">(.*?)</ul>'
    news = re.findall(reg, html, re.S|re.M)
    if(len(news) == 1):
        return extractItems(news[0])
    return None

'''
提取豆瓣首页里面的新闻链接地址和标题
'''
def extractItems(content):
    reg = r'<li>(.*?)</li>'
    linkReg = re.compile(reg)
    linkList = re.findall(linkReg, content)
    news = []
    for link in linkList:
        itemReg = re.compile('<a href="(.*?)">(.*?)</a>')
        match = itemReg.match(link)
        if match:
            item = []
            item.append(match.group(1))
            item.append(match.group(2))
            news.append(item)
    return news 

'''
提取新闻里面的内容
'''
def extractMeta(html):
    meta = {}
    meta['title'] = ''
    meta['author'] = ''
    meta['pubTime'] = ''
    meta['content'] = ''
    
    #1. 提取标题
    titleReg = r'<h1>(.*?)</h1>'
    titles = re.findall(titleReg, html, re.S|re.M)
    if titles:
        meta['title'] = titles[0]
    
    #2. 提取作者
    authorReg = r'class="note-author">(.*?)</a>'
    authors = re.findall(authorReg, html, re.S|re.M)
    if authors:
        meta['author'] = authors[0]
    
    #3. 提取时间
    timeReg = r'class="pub-date">(.*?)</span>'
    times = re.findall(timeReg, html, re.S|re.M)
    if authors:
        meta['pubTime'] = times[0]
        
    #4. 提取内容
    contentReg = r'id="link-report">(.*?)<div class="copyright-claim original">'
    contents = re.findall(contentReg, html, re.S|re.M)
    if contents:
        meta['content'] = strip_tags(contents[0])
    return meta

'''
提取文本
'''
def strip_tags(html):  
    result = ['']  
    parser = HTMLParser()  
    parser.handle_data = result.append  
    parser.feed(html)  
    parser.close()  
    return ''.join(result).strip() 
