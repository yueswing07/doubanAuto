# !/usr/bin/python3
# coding=utf-8

# -----------------------爬虫-------------
# pip3 install requests pip3 install lxml
# 系统标准库
import sys
import re
from time import sleep
from urllib.parse import urlencode,urljoin
import json
import random
import string

#第三方模块
import requests 
# from lxml import html
# from pyquery import PyQuery as pq

# 自建模块
from util import cookie as CookieModule

CONFIG = {
    'topicUrl' : ['https://www.douban.com/group/topic/122476784/']
}
headers = {
    "Host": "www.douban.com",
    "Origin": "https://www.douban.com",
    # "Referer": CONFIG['topicUrl'][0]+"?start=0",
    # "Upgrade-Insecure-Requests": '1',
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
}

# cookie set 
cookiesStr = 'bid=ZneGZ9dF008; ll="108288"; _ga=GA1.2.509933802.1529456369; __yadk_uid=7KhWXonEVAUOamdRoD13vwz0nwAUdglp; ap=1; _vwo_uuid_v2=D7203DB0D34A627D8C0CD470DECF6EA94|1eeacdeabfa10beda79f08e1753db37b; gr_user_id=5f3e7fc5-8dcf-48d1-968e-bc171bfd66f3; douban-fav-remind=1; douban-profile-remind=1; __utmv=30149280.16660; __utmz=30149280.1531553870.3.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ct=y; __utmc=30149280; dbcl2="166602750:9/3V6YQsUuY"; ck=hI_f; ap_6_0=1; ap_6_0_1=1; push_doumail_num=0; push_noty_num=0; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1534597884%2C%22https%3A%2F%2Fmusic.douban.com%2Fsubject%2F30166746%2F%22%5D; _pk_ses.100001.8cb4=*; ap_v=1,6.0; __utma=30149280.509933802.1529456369.1534485739.1534597885.122; ps=y; __utmt=1; _pk_id.100001.8cb4=eb21927d75c14542.1529456368.232.1534598970.1534500606.; __utmb=30149280.395.9.1534598970868'
cookie = CookieModule.Cookie(cookiesStr)


# *******************************发帖编辑***************************
url = 'https://www.douban.com/j/group/topic/publish'
title = '恩'
# text = '恩'
textBlock = {
    "key": ''.join(random.sample(string.ascii_letters + string.digits, 5)),
    "text": "小组置顶：https://www.douban.com/group/topic/111306566/ \n https://www.douban.com/group/topic/40513407/ \n https://www.douban.com/group/topic/112936376/ \n\n 福利暂定：  \n\n 备注：管理勿删除 机器自动发帖  ",
    "type": "unstyled",
    "depth": 0,
    "inlineStyleRanges": [],
    "entityRanges": [],
    "data": {}
    }
content = {
    "blocks":[textBlock],
    "entityMap":{}
}
contentJsonStr = json.dumps(content)
multipartPayload = {
    "ck": (None, cookie.get('ck')),
    "title": (None,title),
    "content": (None,contentJsonStr),
    # "captcha-solution": verify_code,
    # "captcha-id": pic_id,
    "group_id": (None,"10479"),
    "topic_id":(None,"122476784")
}
response = requests.post(url, files=multipartPayload, headers=headers, cookies=cookie.getAll())
print(response.text)
# {"url":"https:\/\/www.douban.com\/group\/topic\/122472967\/","r":0}
print(response.request.body)
print(response.request.headers)
sys.exit(0)


# *******************************发帖***************************
url = 'https://www.douban.com/j/group/topic/publish'
title = '恩'
# text = '恩'
textBlock = {
    "key": ''.join(random.sample(string.ascii_letters + string.digits, 5)),
    "text": "恩",
    "type": "unstyled",
    "depth": 0,
    "inlineStyleRanges": [],
    "entityRanges": [],
    "data": {}
    }
content = {
    "blocks":[textBlock],
    "entityMap":{}
}
contentJsonStr = json.dumps(content)
multipartPayload = {
    "ck": (None, cookie.get('ck')),
    "title": (None,title),
    "content": (None,contentJsonStr),
    # "captcha-solution": verify_code,
    # "captcha-id": pic_id,
    "group_id": (None,"10479")
}
response = requests.post(url, files=multipartPayload, headers=headers, cookies=cookie.getAll())
print(response.text)
# {"url":"https:\/\/www.douban.com\/group\/topic\/122472967\/","r":0}
print(response.request.body)
print(response.request.headers)
sys.exit(0)


# *******************************删回复***************************通过
url = 'https://www.douban.com/j/group/topic/111306566/remove_comment'
# https://www.douban.com/j/group/topic/111306566/remove_comment
payload  = {
    "cid": "1675174562",
    "ck": cookie.get('ck')
}
response = requests.post(url, data=payload , headers=headers, cookies=cookie.getAll(),
                      )
print(response.text)
sys.exit(0)

# *******************************回复***************************通过
topicUrl = CONFIG['topicUrl']
comment_topic_url = topicUrl[0] + "add_comment"
rv_comment = "北五 支持 北五 up "
verify_code = ''
pic_id = ''
comment_dict = {
    "ck": cookie.get('ck'),
    "rv_comment": rv_comment,
    "start": 0,
    # "captcha-solution": verify_code,
    # "captcha-id": pic_id,
    "submit_btn": "发送"
}
response = requests.post(comment_topic_url, files='', headers=headers, cookies=cookie.getAll(),
                      data=comment_dict,verify=False)
print(response.text)
sys.exit(0)




# # python 请求cookie 处理  1. 请求设置 可以在请求函数的参数传递 cookies=cookiesDit 参数。
# # 2. 获取返回cookie 再返回的请求对象中获取rs.cookies.get_dict() 注意只有后台返回设置了cookie 才能获取到
# # 公用  http://cn.python-requests.org/zh_CN/latest/user/quickstart.html#cookie
# headers = {
#   "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
# }
# LOGIN_URL = 'http://192.168.2.251/TPJoyschoolLc/Home/Login/login'
# SCHOOL_URL = 'http://192.168.2.251/TPJoyschoolLc/Home/SchoolManager/schoolSearch'
# cookiesDit = {
#   'PHPSESSID':'d38k25b2nt90ahhaanuuqghrh6'
# }
# requests = requestsModule.session()
# print(type(requests))
# print(type(requests))
# print(requests.cookies.get_dict())#先打印一下，此时一般应该是空的。
# postData ={
#   'request': 'schoolSearch',
#   'keyWord': '',
#   'projectManager': '',
#   'pageSize': 10,
#   'pageSN': 1
# }
# # 设置了 cookies
# rs=requests.post(SCHOOL_URL,data = postData,headers=headers,cookies=cookiesDit,verify=False)
# rs.encoding='utf-8'
# print(requests.cookies.get_dict() )

# # print(json.loads(rs.text))
# print(rs.headers )
# # 服务端设置了cookie 可以获取
# print(rs.cookies.get_dict() )
# # print(rs.cookies['PHPSESSID'] )
# print(json.loads(rs.content) )

# print(requests)
# print(rs)
# print(rs==requests)
# # c=requestsModule.cookies.RequestsCookieJar()#利用RequestsCookieJar获取
# # c.set('cookie-name','cookie-value')
# # requests.cookies.update(c)
# # print(requests.cookies.get_dict())
# # print(requests.cookies.values())
# sys.exit(0)

