from urllib import request
import re
import random
#构建处理器对象（专门处理请求的对象）
http_hander=request.HTTPHandler()

#创建一个自定的opener
opener=request.build_opener(http_hander)


#创建请求对象
url=r'http://www.baidu.com/'
req=request.Request(url)
#提交请求，获取响应
reponse=opener.open(req).read()#自定义 ，取代“urllib.request.urlopen(req)”

#把自定义的opener设置为全局，这样用urlopen发送的请求也会使用自定的opener
request.install_opener(opener)#设置为全局

reponse=request.urlopen(req).read()

print(reponse)


