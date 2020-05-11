'''
1、知名端口（0~1023）：
80 HTTP服务（浏览器）
21 FTP服务（）
3306 mysql数据库
4000~QQ（动态）
2、动态端口号（1024~65525）：
3、127.0.0.1~127.255.255.255用于回路测试，
如：127.0.0.1可以代表本机IP地址，
用http://127.0.0.1就可以测试本机中配置的Web服务器
'''
import socket
#生成socket链接对象
clint=socket.socket()
clint.connect(('localhost',6969))#和目标主机建立链接
clint.send('hello word!'.encode())#向对方发送数据
clint.close()
