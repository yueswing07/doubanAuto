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

while (1):
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
                          data=comment_dict)
    sleep(random.randint(70,79))

#print(response.text)
sys.exit(0)