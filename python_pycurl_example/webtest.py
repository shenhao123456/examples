# -*- coding: utf-8 -*-
# File Name：    webtest
# Description :   
# Author :       shenhao
# date：         2019/7/2
def curl_webSev(URL='www.ipython.me'):
    _Curl = pycurl.Curl()
    _Curl.setopt(pycurl.CONNECTTIMEOUT, 5)
    _Curl.setopt(pycurl.TIMEOUT, 5)
    _Curl.setopt(pycurl.NOPROGRESS, 1)
    _Curl.setopt(pycurl.FORBID_REUSE, 1)
    _Curl.setopt(pycurl.MAXREDIRS, 1)
    _Curl.setopt(pycurl.DNS_CACHE_TIMEOUT, 30)
    _Curl.setopt(pycurl.URL, URL)
    try:
        with open(os.path.dirname(os.path.realpath(__file__)) + "/content.txt", 'w') as outfile:
            _Curl.setopt(pycurl.WRITEHEADER, outfile)
            _Curl.setopt(pycurl.WRITEDATA, outfile)
            _Curl.perform()
    except Exception as err:
        print("exec error!\n\t%s" % err)
        sys.exit()
    print("Http Code:\t%s" % _Curl.getinfo(_Curl.HTTP_CODE))
    print("DNS lookup time:\t%s ms" % (_Curl.getinfo(_Curl.NAMELOOKUP_TIME) * 1000))
    print("Create conn time:\t%s ms" % (_Curl.getinfo(_Curl.CONNECT_TIME) * 1000))
    print("Ready conn time:\t%s ms" % (_Curl.getinfo(_Curl.PRETRANSFER_TIME) * 1000))
    print("Tran Star time:\t%s ms" % (_Curl.getinfo(_Curl.STARTTRANSFER_TIME) * 1000))
    print("Tran Over time:\t%s ms" % (_Curl.getinfo(_Curl.TOTAL_TIME) * 1000))
    print("Download size:\t%d bytes/s" % _Curl.getinfo(_Curl.SIZE_DOWNLOAD))
    print("HTTP header size:\t%d byte" % _Curl.getinfo(_Curl.HEADER_SIZE))
    print("Avg download speed:\t%s bytes/s" % _Curl.getinfo(_Curl.SPEED_DOWNLOAD))



if __name__ == '__main__':
    import os
    import sys
    import time
    import pycurl

    if sys.argv[1]:
        curl_webSev(sys.argv[1])
    else:
        curl_webSev()

# c = pycurl.Curl()    #创建一个curl对象
#
# c.setopt(pycurl.CONNECTTIMEOUT, 5)    #连接的等待时间，设置为0则不等待
#
# c.setopt(pycurl.TIMEOUT, 5)           #请求超时时间
#
# c.setopt(pycurl.NOPROGRESS, 0)        #是否屏蔽下载进度条，非0则屏蔽
#
# c.setopt(pycurl.MAXREDIRS, 5)         #指定HTTP重定向的最大数
#
# c.setopt(pycurl.FORBID_REUSE, 1)      #完成交互后强制断开连接，不重用
#
# c.setopt(pycurl.FRESH_CONNECT,1)      #强制获取新的连接，即替代缓存中的连接
#
# c.setopt(pycurl.DNS_CACHE_TIMEOUT,60) #设置保存DNS信息的时间，默认为120秒
#
# c.setopt(pycurl.URL,"http://www.baidu.com")      #指定请求的URL
#
# c.setopt(pycurl.USERAGENT,"Mozilla/5.2 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50324)")    #配置请求HTTP头的User-Agent
#
# c.setopt(pycurl.HEADERFUNCTION, getheader)   #将返回的HTTP HEADER定向到回调函数getheader
#
# c.setopt(pycurl.WRITEFUNCTION, getbody)      #将返回的内容定向到回调函数getbody
#
# c.setopt(pycurl.WRITEHEADER, fileobj)        #将返回的HTTP HEADER定向到fileobj文件对象
#
# c.setopt(pycurl.WRITEDATA, fileobj)          #将返回的HTML内容定向到fileobj文件对象
#
# c.getinfo(pycurl.HTTP_CODE)         #返回的HTTP状态码
#
# c.getinfo(pycurl.TOTAL_TIME)        #传输结束所消耗的总时间
#
# c.getinfo(pycurl.NAMELOOKUP_TIME)   #DNS解析所消耗的时间
#
# c.getinfo(pycurl.CONNECT_TIME)      #建立连接所消耗的时间
#
# c.getinfo(pycurl.PRETRANSFER_TIME)  #从建立连接到准备传输所消耗的时间
#
# c.getinfo(pycurl.STARTTRANSFER_TIME)    #从建立连接到传输开始消耗的时间
#
# c.getinfo(pycurl.REDIRECT_TIME)     #重定向所消耗的时间
#
# c.getinfo(pycurl.SIZE_UPLOAD)       #上传数据包大小
#
# c.getinfo(pycurl.SIZE_DOWNLOAD)     #下载数据包大小
#
# c.getinfo(pycurl.SPEED_DOWNLOAD)    #平均下载速度
#
# c.getinfo(pycurl.SPEED_UPLOAD)      #平均上传速度
#
# c.getinfo(pycurl.HEADER_SIZE)       #HTTP头部大小
