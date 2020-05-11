from urllib import request
import urllib

url='https://exmail.qq.com'

headers={
	
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362',
   'Cookie':'pt_local_token=2-; pgv_info=ssid=s3483316844; qm_authimgs_id=2; qm_verifyimagesession=h01a8a11b5f8f7addcd21c60eca61196dd654748a8f37d84e23ca2e577a75dc4ef1acb0a314bbf20ce4; dm_login_weixin_rem=; pgv_pvid=8164341820; pgv_pvi=5462284288; logout_page=dm_loginpage; ssl_edition=mail.qq.com; Hm_lpvt_bdfb0d7298c0c5a5a2475c291ac7aca2=1588691849; 0.91623262063225; tinfo=1588690986.0000*; _gid=GA1.3.1292022537.1588690898; _ga=GA1.3.1299135268.1586086670; Hm_lvt_bdfb0d7298c0c5a5a2475c291ac7aca2=1588690898; _gat=1'
}

req=request.Request(url,headers=headers)
response=request.urlopen(req)
print(response.read().decode())