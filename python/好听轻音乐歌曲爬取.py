#好听轻音乐网：http://www.htqyy.com/
import re		#python的正则库
import requests	#python的requests库
import time		#
import lxml.html

#榜单第一页url
#请求 URL: http://www.htqyy.com/top/hot
#榜单第二页url
#http://www.htqyy.com/top/musicList/hot?pageIndex=1&pageSize=20
#榜单第三页url
#http://www.htqyy.com/top/musicList/hot?pageIndex=2&pageSize=20

#单曲资源url
#http://f2.htqyy.com/play7/658/mp3/5

songID=[]
songName=[]

for i in range(0,26):
	url='http://www.htqyy.com/top/musicList/hot?pageIndex='+str(i)+'&pageSize=20'
	
	#获取音乐榜单的网页信息
	html=requests.get(url)


	strr=html.text

	pat1=r'title="(.*?)" sid'
	pat2=r'sid="(.*?)"'

	idlist=re.findall(pat2,strr)
	titlelist=re.findall(pat1,strr)
	songID.extend(idlist)
	songName.extend(titlelist)								
for i in range(0,len(songName)):								#对html实体进行解码（‘&#39’：‘’’）
	songName[i]=lxml.html.fromstring(songName[i]).text_content()#

for i in range(0,len(songID)):
	songurl='http://f2.htqyy.com/play7/'+str(songID[i])+'/mp3/5'
	songname=songName[i]

	data=requests.get(songurl).content

	print('正在下载第',i+1,'首')

	with open('D:\\music\\{}.mp3'.format(songname),'wb') as f:
		f.write(data)
	time.sleep(0.5)