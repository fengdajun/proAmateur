from multiprocessing import Process
import time

def run(name):
	print(name,'进程执行了')
	time.sleep(5)

if __name__ == '__main__':
	#创建进程
	p1=Process(target=run,args=('p1',))
	p2=Process(target=run,args=('p2',))
	p3=Process(target=run,args=('p3',))
	p4=Process(target=run,args=('p4',))
	p5=Process(target=run,args=('p5',))
	p6=Process(target=run,args=('p6',))
	p7=Process(target=run,args=('p7',))


	p1.start()
	p2.start()
	p3.start()
	p4.start()
	p5.start()
	p6.start()
	p7.start()
#多进程可以真正实现同一时间多个任务并行（windows需要如此处理，linux不要）
