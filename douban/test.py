import requests as requestsModule
cookiesDit = {
  'PHPSESSID':'d38k25b2nt90ahhaanuuqghrh6'
}
requests = requestsModule.session()
print(requests.cookies.get_dict()) #先打印一下，此时一般应该是空的。
postData ={
}
# 设置了 cookies
rs=requests.post('http://www.baidu.com',data = postData,headers=headers,cookies=cookiesDit,verify=False)
rs.encoding='utf-8'
print(requests.cookies.get_dict() )
print(rs.cookies.get_dict() )

import requests as requestsModule
cookiesDit = {
  'PHPSESSID':'d38k25b2nt90ahhaanuuqghrh6'
}
requests = requestsModule.session()
requestsModule.utils.add_dict_to_cookiejar(requests.cookies, cookiesDit)
print(requests.cookies.get_dict()) #先打印一下，此时一般应该是空的。
postData ={
}
# 设置了 cookies
rs=requests.post('http://www.baidu.com',data = postData,headers=headers,cookies=cookiesDit,verify=False)
rs.encoding='utf-8'
print(requests.cookies.get_dict() )
print(rs.cookies.get_dict() )

c=requests.cookies.RequestsCookieJar()#利用RequestsCookieJar获取
c.set('cookie-name','cookie-value')
s.cookies.update(c)




#  post请求 调用成功
cookiesDit = {
  'PHPSESSID':'c32nml1botj5a77c45v4lcmjb1'
}
postData ={
    "request": "schoolSearch",
    # keyWord: 
    # projectManager: 
    "pageSize": 10,
    "pageSN": 1
}
rs=requests.post('https://joyclass.51joyshow.com/Home/SchoolManager/schoolSearch',data = postData,headers=headers,cookies=cookiesDit)


# *******************************回复
url = 'https://www.douban.com/group/topic/111306566/add_comment#last'
# https://www.douban.com/j/group/topic/111306566/remove_comment
rv_comment = "七哥 自动帮你顶帖 "
verify_code = ''
pic_id = ''
payload = {
    "ck": (None,cookie.get('ck')),
    "rv_comment": (None,rv_comment),
    "start": (None,0),
    # "captcha-solution": verify_code,
    # "captcha-id": pic_id,
    "submit_btn": (None,"发送")
}
cookiesDit = cookie.getAll()
headers['Accept'] =  'text/plain, */*; q=0.01'
headers['Accept-Encoding'] = 'gzip, deflate, br'
headers['Accept-Language'] =  'zh-CN,zh;q=0.9'
response = requests.post(url, files=payload , headers=headers, cookies=cookiesDit)
print(response.text)

# *******************************删回复
url = 'https://www.douban.com/j/group/topic/119999985/remove_comment'
# https://www.douban.com/j/group/topic/111306566/remove_comment
payload  = {
    "cid": "1639409293",
    "ck": cookie.get('ck')
}
# headers["Content-Type"] = "application/x-www-form-urlencoded"
# print(headers)
# print(url)
# print(data)
# print(cookie.getAll())
# sys.exit(0)
cookiesDit = cookie.getAll()
response = requests.post(url, data=payload , headers=headers, cookies=cookiesDit)
print(response.text)

# ******************************* 发帖
# url = 'https://www.douban.com/group/beijing/new_topic'
url = 'https://www.douban.com/j/group/topic/publish'
title = '恩'
text = '恩'
payload = {
    "ck": cookie.get('ck'),
    "title": title,
    "content": text,
    # "captcha-solution": verify_code,
    # "captcha-id": pic_id,
    "group_id": "10479"
}

# application/x-www-form-urlencoded
response = requests.post(url, data=payload , headers=headers, cookies=cookiesDit)
print(response.text)
print(response.request.body)
print(response.request.headers)

url = 'https://www.douban.com/j/group/topic/publish'
title = '恩'
text = '恩'
payload = {
    "ck": cookie.get('ck'),
    "title": title,
    "content": text,
    # "captcha-solution": verify_code,
    # "captcha-id": pic_id,
    "group_id": "10479"
}

# application/x-www-form-urlencoded
response = requests.post(url, data=payload , headers=headers, cookies=cookiesDit)
print(response.text)
print(response.request.body)
print(response.request.headers)

multipartPayload = {
    "ck": (None, cookie.get('ck')),
    "title": (None,title),
    "content": (None,text),
    # "captcha-solution": verify_code,
    # "captcha-id": pic_id,
    "group_id": (None,"10479")
}
response = requests.post(url, files=multipartPayload, headers=headers, cookies=cookiesDit)
print(response.text)
print(response.request.body)
print(response.request.headers)

# multipart/form-data请求
# https://blog.csdn.net/yu12377/article/details/77188895


import sys
import re
import requests 
from time import sleep
# from lxml import html
# from pyquery import PyQuery as pq

from urllib.parse import urlencode,urljoin
import json

# 
from util import cookie as CookieModule


headers = {
    "Host": "www.douban.com",
    "Origin": "https://www.douban.com",
    # "Referer": CONFIG['topicUrl'][0]+"?start=0",
    # "Upgrade-Insecure-Requests": '1',
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
}


账号1：

cookiesStr = '_ga=GA1.2.694242279.1529456325; bid=rf5vQ_9E9-g; __utmc=30149280; ll="108288"; ue="yue017@126.com"; push_doumail_num=0; __utmv=30149280.8443; ap=1; _vwo_uuid_v2=DF8A33991A83A2F3E5B303BB32FECF5BE|efb0cf49460c216a421f7d0b1519e98a; gr_user_id=248acb57-c4d7-4535-8376-119c3da3562a; dbcl2="84433341:NS/iTmtstlA"; ck=_XgG; push_noty_num=0; ct=y; __yadk_uid=iNZuiaieXLBc6CqH8sbgBqKBW4yJ3n2d; douban-fav-remind=1; douban-profile-remind=1; __utmz=30149280.1531981688.42.14.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1532590035%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DsRZhTClyJnfxHitVspM1UfiAyQGp_E03caxSxc-8LZU6Ez2lzgctKrDlk6AOknk1fwDyzTomyuLI6C6uYA_Og_%26wd%3D%26eqid%3D9a9c5c5d000737a1000000025b474e96%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.694242279.1529456325.1532567960.1532590038.58; __utmb=30149280.32.10.1532590038; _pk_id.100001.8cb4=505482db92ab0394.1531205992.42.1532593490.1532567983.'
cookie = CookieModule.Cookie(cookiesStr)
cookiesDit = cookie.getAll()

aa = requests.get('https://www.douban.com/',headers=headers,cookies=cookiesDit)


账号2：

cookiesStr = 'bid=ZneGZ9dF008; ll="108288"; _ga=GA1.2.509933802.1529456369; __yadk_uid=7KhWXonEVAUOamdRoD13vwz0nwAUdglp; ap=1; _vwo_uuid_v2=D7203DB0D34A627D8C0CD470DECF6EA94|1eeacdeabfa10beda79f08e1753db37b; gr_user_id=5f3e7fc5-8dcf-48d1-968e-bc171bfd66f3; ck=LISO; douban-fav-remind=1; douban-profile-remind=1; __utmc=30149280; __utmv=30149280.16660; __utmz=30149280.1531553870.3.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ps=y; session=VGn4SE69ID1kNOsT_C2AHoAFOBCXYUEesy7IphEjQwQ7b5UsvliHiZlJmTd3Xa4aU_FhQSMClzRDEcVMeDUGyIACSohjU1tHQdbU2OIUFK19cQFVBXN0YXRlcQJVCng3OGNVMjFSRDVxA3OHcQQu; ct=y; push_doumail_num=0; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1532569664%2C%22https%3A%2F%2Fmusic.douban.com%2Fsubject%2F30166746%2F%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.509933802.1529456369.1532566321.1532569664.63; push_noty_num=0; _pk_id.100001.8cb4=eb21927d75c14542.1529456368.173.1532573375.1532566973.; __utmb=30149280.235.9.1532573375428'
cookiesStr = 'bid=ZneGZ9dF008; ll="108288"; _ga=GA1.2.509933802.1529456369; __yadk_uid=7KhWXonEVAUOamdRoD13vwz0nwAUdglp; ap=1; _vwo_uuid_v2=D7203DB0D34A627D8C0CD470DECF6EA94|1eeacdeabfa10beda79f08e1753db37b; gr_user_id=5f3e7fc5-8dcf-48d1-968e-bc171bfd66f3; dbcl2="166602750:sTaNOH5RY50"; ck=LISO; douban-fav-remind=1; douban-profile-remind=1; __utmc=30149280; __utmv=30149280.16660; vtd-d="1"; __utmz=30149280.1531553870.3.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ps=y; frodotk_db="15ba9a8e6f32800f412fcfab4d97802d"; session=VGn4SE69ID1kNOsT_C2AHoAFOBCXYUEesy7IphEjQwQ7b5UsvliHiZlJmTd3Xa4aU_FhQSMClzRDEcVMeDUGyIACSohjU1tHQdbU2OIUFK19cQFVBXN0YXRlcQJVCng3OGNVMjFSRDVxA3OHcQQu; ct=y; push_doumail_num=0; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1532584683%2C%22https%3A%2F%2Fmusic.douban.com%2Fsubject%2F30166746%2F%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.509933802.1529456369.1532581251.1532584683.65; __utmt=1; push_noty_num=0; _pk_id.100001.8cb4=eb21927d75c14542.1529456368.175.1532587630.1532582491.; __utmb=30149280.310.9.1532587630416'
cookie = CookieModule.Cookie(cookiesStr)
cookiesDit = cookie.getAll()

aa = requests.get('https://www.douban.com/',headers=headers,cookies=cookiesDit)
aa.text.find('七哥')

备注: 大坑 document.cookie  获取的cookie  和  从请求拿的cookie 不一样 前者不行。应该是少了dbcl2字段。


