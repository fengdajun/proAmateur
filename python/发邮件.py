'''
常用电子邮件协议有SMTP POP3 IMAP4，
他们都隶属于TCP/IP簇，
默认状态下，分别通过TCP端口25、110、143建立连接。
'''
'''
准备工作:
安装第三方模块（pip install pyemail）
邮件发送方（发送方地址（fengdj@itocec.com），
发送方客户端授权密码（JqvdGfhkaZdEMFCd），
SMTP服务器地址(smtp.exmail.qq.com)）(使用SSL，端口号465)
邮件内容
邮件接受方
'''
#引入模块
import smtplib
from email.mime.text import MIMEText
msg_from='fengdj@itocec.com'#发送方
psw='JqvdGfhkaZdEMFCd'#授权密码
#to='790531101@qq.com'#发到QQ邮箱
to='fengdj@itocec.com'#自发自收

subject='这是一封邮件'
#content='你中奖了！'
content='<h1>你中奖了！</h1>'#用网页方式发送（加粗字体）
#构造邮件
#msg=MIMEText(content)#msg邮件对象
msg=MIMEText(content,'html','utf-8')#msg邮件对象，用网页方式发送（加粗字体）
msg['Subject']=subject#邮件，主题类似于字典
msg['From']=msg_from
msg['To']=to

#发送邮件
try:
	ss=smtplib.SMTP_SSL('smtp.exmail.qq.com',465)
	ss.login(msg_from,psw)
	ss.sendmail(msg_from,to,msg.as_string())#发送
	print('发送成功！')
except Exception as e:
	print('发送失败！详情：',e)

