#json用于不同系统间或者同一系统的前端与后台间的数据通讯
#简单来讲，json就是js（Java Script）中的对象
#数据结构：{key:value,key:value......}(字典)
#本质上讲，json就是有特定结构的字符串

import json

#json转字典
j='{"city":"北京","name":"熊猫"}'
print(type(j))
p=json.loads(j)
print(p)
print(type(p))

#字典转json
dictt={"city":"北京","name":"熊猫"}
ss=json.dumps(dictt,ensure_ascii=False)
print(ss)
print(type(ss))

