# -*- coding: GB18030 -*-
# ��һ�м�����󣬾Ϳ��Լ�����ע����
'''
Created on 2017��5��21��

@author: tony
'''
from util import CommonUtil, FileUtil, FetcherUtil, MysqlUtil, HtmlExtract
import sys
reload(sys)
sys.setdefaultencoding(CommonUtil.GB18030)

'''
�򵥵�ͨ��cookieץȡ΢���������
'''
if __name__ == '__main__':
    #1. ��ʼ������
    url = 'http://s.weibo.com/weibo/%25E4%25BA%25AC%25E4%25B8%259C&b=1&page=1'
    cookie_str = '������д�Լ���΢���˺�cookie'
    #2. ���ȴ�Mysql�л�ȡ����
    urlSum = CommonUtil.getUrlSum(url)
    html = MysqlUtil.getHtml(urlSum)
    #3. ���Mysqlû�п��գ���ʵʱ�Ĵ�����ץȡ����
    if not html:
        html = FetcherUtil.fetchWeibo(url, cookie_str)
        result = MysqlUtil.saveHtml(urlSum, url, html) #ץȡ�����պ�洢����Mysql��
        if result:
            print '����΢�����ճɹ�'
        else:
            print '����΢������ʧ��'
    
    FileUtil.writeLine("weibo.html", html) #������յ���ʱ�ļ���
    #4. ��html��������ȡ�ṹ����΢������
    weiboDatas = HtmlExtract.extractWeiboContent(html) 
    #5. ������ȡ����΢���ṹ������
    for weiboData in weiboDatas:
        print '����:'.decode(CommonUtil.GB18030), weiboData['author']
        print '����ʱ��:'.decode(CommonUtil.GB18030), weiboData['pubTime']
        print '����:'.decode(CommonUtil.GB18030), weiboData['text'].encode(CommonUtil.GB18030)
        print ''
    print '�ҵ�'.decode(CommonUtil.GB18030), len(weiboDatas), '��΢��'.decode(CommonUtil.GB18030)
    #6. �洢��Mysql��