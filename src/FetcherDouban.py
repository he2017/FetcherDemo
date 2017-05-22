# -*- coding: utf-8 -*-
from time import ctime, sleep
import MySQLdb
import httplib
import re
import sys
import threading
import urllib
import urlparse
reload(sys)
sys.setdefaultencoding('utf-8')


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def extractContent(html):
    reg = r'class="notes">(.*?)</ul>'
    dir = re.findall(reg, html, re.S|re.M)
    if(len(dir) == 1):
        return dir[0]
    else:
        return None
    
def extractTitle(content):
    reg = r'<h1>(.*?)</h1>'
    titles = re.findall(reg, content, re.S|re.M)
    for title in titles:
        print title

def extractItems(content):
    reg = r'<li>(.*?)</li>'
    linkReg = re.compile(reg)
    linkList = re.findall(linkReg, content)
    
    print len(linkList)
    
    items = []
    for link in linkList:
        itemReg = re.compile('<a href="(.*?)">(.*?)</a>')
        match = itemReg.match(link)
        if match:
            item = []
            item.append(match.group(1))
            item.append(match.group(2))
            items.append(item)
            print item[0]
            print item[1]
    return items  

def saveItems(items):
    try:
        conn = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='fetcher_data', port=3306, charset="utf8")
        cur = conn.cursor()
        for item in items:
            sql = "insert into dir_test (url, title) values('%s', '%s')"%(item[0],item[1])
            cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def getUrls():
    urls = []
    try:
        conn = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='fetcher_data', port=3306, charset="utf8")
        cur = conn.cursor()
        cur.execute('select * from dir_test')
        results = cur.fetchmany(10)
        for r in results:
            urls.append(r[1])
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    return urls


def doTask():
    while True:
        urls = getUrls()
        for url in urls:
            itemHtml = getHtml(url)
            extractTitle(itemHtml)
        sleep(5) 

def request(url, cookie=''):
    ret = urlparse.urlparse(url)    # Parse input URL
    conn = httplib.HTTPConnection(ret.netloc)
    conn.request(method='GET', url=url , headers={'Cookie': cookie})
    return conn.getresponse()

def writeLine(fileName, line):
        try:
            fObj = open(fileName, 'w+')
            fObj.write(line)
            fObj.write('\n')
            fObj.close()
            print 'write successfully'
        except IOError, e:
            print 'file write error:', e, 'line:', line
            
def fetchWeibo():
    cookie_str = 'SINAGLOBAL=2204125497955.829.1485329104913; wvr=6; UOR=,,cuiqingcai.com; SSOLoginState=1495344721; SCF=Ah6FvK5u7EHN9tYhyolKNjlJFG4syHY2CW9__5jrTG_w8LMsQbZmqhFiQrlpLRHFBqAIBMmUL7YrU_I8Y2Vw8ns.; SUB=_2A250JVYBDeThGeNI6VQV-SbJzD2IHXVXU8DJrDV8PUNbmtANLRGhkW-YMpXkX0BaJ0OgHXhkwbiSBCowlQ..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFv6clAKgcmksgpb_WU.yRA5JpX5KMhUgL.Fo-ceoqX1KnfS022dJLoI7LQ9Hv3Ug4N9g.t; SUHB=00x5C_V77tCjcU; ALF=1526880719; SWB=usrmdinst_15; _s_tentry=weibo.com; Apache=4198956184554.845.1495344744878; ULV=1495344744894:53:10:1:4198956184554.845.1495344744878:1495294801627; NSC_wjq_txfjcp_mjotij=ffffffff094113d645525d5f4f58455e445a4a423660; WBStorage=02e13baf68409715|undefined'
    url = 'http://s.weibo.com/weibo/%25E4%25BA%25AC%25E4%25B8%259C&b=1&page=2'
    html_doc = request(url, cookie_str).read()
    writeLine("test.html", html_doc)
    return html_doc

def ayncFetchUrl():
    thread1 = threading.Thread(target=doTask)
    thread2 = threading.Thread(target=doTask)
    thread1.setDaemon(False)
    thread1.start()
    thread2.setDaemon(False)
    thread2.start()
    print "all over"

def readLines(fileName):
    lines = []
    try:
        fObj = open(fileName, 'r')
        for eachLine in fObj:
            eachLine = eachLine.strip('\n')
            lines.append(eachLine)
        fObj.close()
    except IOError, e:
        print 'file open error:', e
    finally:
        return lines
    
def extractWeiboContent(html):
    reg = r'<div class=\\"WB_feed_detail clearfix\\">(.*?)<div class=\\"feed_action'
    itemList = re.findall(reg, html, re.S|re.M)
    print itemList
    for item in itemList:
        itemReg = r'nick-name=\\"(.*?)\\"'
        nickNames = re.findall(itemReg, item, re.S|re.M)
        print nickNames
        for nickName in nickNames:
            print nickName.decode()
        
if __name__ == '__main__':
    #ayncFetchUrl()
    html = fetchWeibo()
    extractWeiboContent(html)
    
    #url = 'https://www.douban.com/'
    #html = getHtml(url)
    #print html
    #content = extractContent(html)
    #items = extractItems(content)
    #saveItems(items)

