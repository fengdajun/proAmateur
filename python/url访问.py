import time
from urllib import request

url="https://www.baidu.com"

data=request.urlopen(url).read()
try:
	print(data.decode(encoding='cp936',errors='strict'))
except Exception as e:
	print('异常',e)
else:
	print('网页读取完毕')
finally:
	print('程序运行结束')

