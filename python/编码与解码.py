#encode()  decode()
#ascii(英) gb2312（中） gbk（中） unicode（各国通用） utf-8（各国通用）
#python3中默认使用utf-8，字符串的两种类型（bytes，str），bytes存储byte类型，str存储unicode类型
#解码decode：bytes-->str
#编码encode：str-->bytes

#编码：字符串转bytes
a='我爱北京天安门'
b1=a.encode('utf-8')
print(b1)

b2=a.encode('gbk')
print(b2)
#解码：bytes-->str(unicode)
c1=b1.decode('utf-8')#编码方式与解码方式要一致
print(c1)

c2=b2.decode('gbk')#编码方式与解码方式要一致
print(c2)


