from urllib import request
import urllib
import random

#处理参数提交
#数字和英文作为参数时不变，汉字作为参数时需要做URL编码

wd={'wd':'北京'} #构造参数字典
url='http://baidu.com/s?'
wdd=urllib.parse.urlencode(wd)#构造url编码
url=url+wdd
print(url)
req=request.Request(url)

reponse=request.urlopen(req).read().decode()

print(reponse)