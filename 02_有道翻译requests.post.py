# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 16:45:37 2018

@author: Admin
"""

import requests
import json

#接收用户输入,将data转码为字节流的形式
key = input('请输入要翻译的内容:')
#1.把Form表单数据整理成字典
data = {
        'i':key,
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':'1542876057778',
        'sign':'11c8155d5d8f185e3c24f7cffa719c3a',
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_REALTIME',
        'typoResult':'false'
        }
#2.urlencode(字典) --> 字符串
#data = urllib.parse.urlencode(data)
#3.字符串.encode("utf-8") --> 字节流
#data = data.encode('utf-8')
#发送请求,获取响应
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}

res = requests.post(url,data=data,headers=headers)
res.encoding = "utf-8"
html = res.text

#print(html) #type(html) is json格式的str
r_dict = json.loads(html)
print(r_dict['translateResult'][0][0])


