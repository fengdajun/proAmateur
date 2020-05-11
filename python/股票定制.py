import tushare#股票模块
import time#时间模块
import smtplib#邮件模块
from email.mime.text import MIMEText#邮件模块
#获取股票数据函数
def getrealtimedata(share):
	dataNow=tushare.get_realtime_quotes(share.code)
	share.price=dataNow.loc[0][3]
	share.name=dataNow.loc[0][0]
	share.high=dataNow.loc[0][4]
	share.low=dataNow.loc[0][5]
	share.volumn=dataNow.loc[0][8]
	share.amount=dataNow.loc[0][9]
	share.openToday=dataNow.loc[0][1]
	share.timeeo=dataNow.loc[0][30]
	share.describe=share.name+'当前价格('+str(share.price)+'元)'
	share.all=dataNow.loc[0][0]+'\t'+dataNow.loc[0][1]+'\t'+dataNow.loc[0][2]+\
	'\t'+dataNow.loc[0][3]+'\t'+dataNow.loc[0][4]+'\t'+dataNow.loc[0][5]+\
	'\t'+dataNow.loc[0][6]+'\t'+dataNow.loc[0][7]+'\t'+dataNow.loc[0][8]+\
	'\t'+dataNow.loc[0][9]+'\t'+dataNow.loc[0][10]+'\t'+dataNow.loc[0][11]+\
	'\t'+dataNow.loc[0][12]+'\t'+dataNow.loc[0][13]+'\t'+dataNow.loc[0][14]+\
	'\t'+dataNow.loc[0][15]+'\t'+dataNow.loc[0][16]+'\t'+dataNow.loc[0][30]
	return share

#股票类
class Share():
	def __init__(self,code,buy,sale):
		self.name=''
		self.price=''
		self.high=''
		self.low=''
		self.volumn=''
		self.openToday=''
		self.pre_close=''
		self.timee=''
		self.describe=''
		self.code=code
		self.buy=buy
		self.sale=sale

#发送邮件函数
def sendemail(subject,content):
	msg_from='fengdj@itocec.com'#发送方
	psw='JqvdGfhkaZdEMFCd'#授权密码
	to1='yuhuan2000@sina.com'#目的邮箱地址1
	to2='790531101@qq.com'#目的邮箱地址2

	#构造邮件
	msg=MIMEText(content)#msg邮件（文本）对象
	#msg=MIMEText(content,'html','utf-8')#msg邮件对象，用网页方式发送（加粗字体）
	msg['Subject']=subject#邮件，主题类似于字典
	msg['From']=msg_from
	msg['To']=to1

	#发送邮件
	try:
		ss=smtplib.SMTP_SSL('smtp.exmail.qq.com',465)
		ss.login(msg_from,psw)
		ss.sendmail(msg_from,to1,msg.as_string())#发送
		print('向',to1,'发送成功！')
		msg['To']=to2
		ss.sendmail(msg_from,to2,msg.as_string())
		print('向',to2,'发送成功！')
	except Exception as e:
		print('发送失败！详情：',e)

def main(sharelist):
	for share in sharelist:
		sss=getrealtimedata(share)
		if float(sss.price)<=sss.buy:
			sendemail('股价定制提醒:达到买点'+sss.describe,sss.all)
		elif float(sss.price)>=sss.sale:
			sendemail('股价定制提醒:达到卖点'+sss.describe,sss.all)
		else:
			pass
while 1==1:

	share1=Share('000066',11.9,12.1)
	share2=Share('600536',76.80,84.00)
	share3=Share('600118',32.9,33.5)

	list1=[share1,share2,share3]
	main(list1)
	time.sleep(300)

