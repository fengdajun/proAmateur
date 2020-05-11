from urllib import request
import re
import random

#反爬虫机制2:判断请求来源的ip地址，如果发觉同一地址高频访问，则禁止
#措施：使用代理ip（本例中使用免费代理182.111.64.7 端口号：41766）
#假定选5个代理ip（本例中重复使用一个）
proxylist=[       			#字典
{'http':'182.111.64.7:41766'},
{'http':'182.111.64.7:41766'},
{'http':'182.111.64.7:41766'},
{'http':'182.111.64.7:41766'},
{'http':'182.111.64.7:41766'},
]

proxy=random.choice(proxylist)

#构建代理处理器对象
proxyHandlaer=request.ProxyHandler(proxy)
#创建自定义opener
opener=request.build_opener(proxyHandlaer)
#创建请求对象
req=request.Request('http://baidu.com')
res=opener.open(req)
print(res.read())

'''
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

#print(reponse)
'''

