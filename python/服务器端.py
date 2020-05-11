import socket
server=socket.socket()
server.bind(('192.168.31.109',6969))#绑定监听的对象
server.listen()#监听
print('准备接电话了。。。')
con,addr=server.accept()#等待消息
print(con,addr)
data=con.recv(1024)
print('接受到的消息是：',data)
server.close()
