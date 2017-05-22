# -*- coding: utf-8 -*-
# 第一行加这个后，就可以加中文注释了
'''
Created on 2017年5月21日

@author: tony
'''
import md5

'''
将url链接转换成md5加密的32位唯一字符串
'''
def getUrlSum(url):
    urlSum = None
    if url:
        url_md5 = md5.new()
        url_md5.update(url)   
        urlSum = url_md5.hexdigest()   
    return urlSum

