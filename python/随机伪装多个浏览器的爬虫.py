import urllib.request#from urllib import request
import re
import random

agent1='Mozilla/5.0 (Linux; U; Android\
 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) A\
 ppleWebKit/537.36 (KHTML, like Gecko) Version/4\
 .0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile S\
 afari/537.36'
agent2='Mozilla/5.0 (Windows NT 10.0; Win64; x64) App\
leWebKit/537.36 (KHTML, like Gecko) Chrome/70.\
.3538.102 Safari/537.36 Edge/18.18362'
agent3='Mozilla/4.0(compatible;MSIE7.0;Windows\
NT5.1;TencentTraveler4.0)'
agent4='Mozilla/4.0(compatible;MSIE7.0;WindowsNT\
5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)'
agent5='Mozilla/4.0(compatible;MSIE7.0;WindowsNT\
5.1;360SE)'

list1=[agent1,agent2,agent3,agent4,agent5]
agent=random.choice(list1)
print(agent)


url=r'http://www.baidu.com/'

'''
#发送请求，获取响应信息,request自动创建请求对象
reponse=urllib.request.urlopen(url).read().decode()#reponse=request.urlopen(url).read()
'''

#自定义请求对象方法(对抗服务器的反爬虫机制)
#例如：
#机制1：通过判断用户是否是通过浏览器访问
#对抗方法：可以通过伪装浏览器进行访问
header={'User-Agent': agent}
req=urllib.request.Request(url,headers=header)
reponse=urllib.request.urlopen(req).read().decode()
#获取title标签中间的内容
pat=r"<title>(.*?)</title>"

data=re.findall(pat,reponse)
print(data)
print(type(data))
print(len(reponse))
print(type(reponse))
#print(reponse)
