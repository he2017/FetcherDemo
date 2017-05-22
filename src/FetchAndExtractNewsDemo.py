# -*- coding:utf-8 -*-  
# 第一行加这个后，就可以加中文注释了
'''
Created on 2017年5月21日

@author: tony
'''
from util import FetcherUtil, HtmlExtract
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
    
if __name__ == '__main__':
    #1. 第一步一个url变量
    url = 'https://www.douban.com/'
    #2. 第二步抓取网页内容
    html = FetcherUtil.fetchHtml(url) 
    #3. 第三步提取链接
    news = HtmlExtract.extractDoubanNews(html)
    #4. 第四步输出提取到的链接和标题
    for item in news:
        print '链接:'.decode("UTF-8"), item[0].decode("UTF-8"), '标题:'.decode("UTF-8"), item[1].decode("UTF-8")
