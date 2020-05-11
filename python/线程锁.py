import threading
import time

lock=threading.Lock()#创建线程锁（互斥锁）

num=100

def run(name):
	lock.acquire()#为当前线程设置锁
	global num#设置num为全局变量
	num=num-1
	print('线程',num,'执行了，目前num值为：',num)
	lock.release()#释放锁

#创建并启动100个线程
for i in range(100):
	t=threading.Thread(target=run,args=(i+1,))
	t.start()

#全局解释器锁（GIL），是python内部的锁，用来保证python程序中统一
#时间点只能执行一个线程（无论计算机处理器内核数量为多少）（计算机处理器为多核时会带来其它问题）
#windows系统使用多进程（而非多线程）来解决GIL造成的弊端

