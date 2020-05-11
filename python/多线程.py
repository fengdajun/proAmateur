import threading
import time

def run(name):
	print(name,'线程执行了')
	time.sleep(5)
#手动创建子线程
t1=threading.Thread(target=run,args=('t1',))
t2=threading.Thread(target=run,args=('t2',))

#启动子线程
t1.start()
t2.start()

t1.join()#设置等待子线程执行完毕后再执行主线程内容
t2.join()


print('执行完毕！')#程序执行时，程序本身就是一个线程，叫做主线程
