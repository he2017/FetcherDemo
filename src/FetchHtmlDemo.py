# -*- coding: GB18030 -*-
# ��һ�м�����󣬾Ϳ��Լ�����ע����
'''
Created on 2017��5��21��

@author: tony
'''
from util import CommonUtil, MysqlUtil, FetcherUtil
import sys
reload(sys)
sys.setdefaultencoding(CommonUtil.GB18030)

if __name__ == '__main__':
    #1. ��һ��һ��url����
    url = 'https://www.douban.com/'
    urlSum = CommonUtil.getUrlSum(url)#��urlת�ɹ̶����ȵ�md5�ַ���
    #2. �ڶ��������ݿ��л�ȡ����
    html = MysqlUtil.getHtml(urlSum)
    if not html:
        #3. ���������ݿ��в������������ʵʱץȡ
        html = FetcherUtil.fetchHtml(url) 
        #4. ����ҳ���ݴ洢��DB
        result = MysqlUtil.saveHtml(urlSum, url, html)
        if result:
            print '������ҳ�ɹ�'.decode(CommonUtil.GB18030)
        else:
            print '������ҳʧ��'.decode(CommonUtil.GB18030)
    if(html):
        print html.encode(CommonUtil.GB18030)
    