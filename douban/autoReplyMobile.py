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
    "Host": "m.douban.com",
    "Origin": "https://m.douban.com",
    # "Referer": CONFIG['topicUrl'][0]+"?start=0",
    # "Upgrade-Insecure-Requests": '1',
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.3",
}

# cookie set 
cookiesStr = '_ga=GA1.3.677640043.1497776871; bid=ZneGZ9dF008; ll="108288"; _ga=GA1.2.509933802.1529456369; ap=1; _vwo_uuid_v2=D7203DB0D34A627D8C0CD470DECF6EA94|1eeacdeabfa10beda79f08e1753db37b; gr_user_id=5f3e7fc5-8dcf-48d1-968e-bc171bfd66f3; douban-fav-remind=1; douban-profile-remind=1; __utmv=30149280.16660; __utmz=30149280.1531553870.3.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ct=y; ap_6_0=1; ap_6_0_1=1; push_doumail_num=0; ps=y; push_noty_num=0; __utma=30149280.509933802.1529456369.1534771508.1534824568.130; __utmc=30149280; dbcl2="166602750:9/3V6YQsUuY"; _gid=GA1.2.1804293999.1534824574; ck=hI_f; ap_v=1,6.0; __utmb=30149280.54.9.1534825043268; talionnav_show_app="0"; frodotk="ef322f293455c341cd968d7b9d0149c3"; talionusr="eyJpZCI6ICIxNjY2MDI3NTAiLCAibmFtZSI6ICJcdTRlMDNcdTU0ZTVcdTVkZjJcdThkNzAifQ=="; _gid=GA1.3.1804293999.1534824574; Hm_lvt_6d4a8cfea88fa457c3127e14fb5fabc2=1534416437,1534825050; _gat_UA-53594431-4=1; _gat_UA-53594431-6=1; Hm_lpvt_6d4a8cfea88fa457c3127e14fb5fabc2=1534825193'
cookie = CookieModule.Cookie(cookiesStr)

# sleep(177)

while (1):
    # *******************************回复***************************通过
    # topicUrl = CONFIG['topicUrl']
    # comment_topic_url = topicUrl[0] + "add_comment"
    comment_topic_url = 'https://m.douban.com/j/add_comment/'
    rv_comment = ''.join(random.sample(string.ascii_letters + string.digits, 17)) + " 北五 支持 北五 up m "+ ''.join(random.sample(string.ascii_letters + string.digits, 7))
    verify_code = ''
    pic_id = ''
    comment_dict = {
        "tid":'122476784',
        "ck": cookie.get('ck'),
        "text": rv_comment,
        # "start": 0,
        # "captcha-solution": verify_code,
        # "captcha-id": pic_id,
        # "submit_btn": "发送"
    }
    response = requests.post(comment_topic_url, files='', headers=headers, cookies=cookie.getAll(),
                          data=comment_dict)
    # if response.status_code !=200:
    #     sleep(777)
    sleep(random.randrange(277,777,77))

#print(response.text)
sys.exit(0)
# nohup python3 autoReplyMobile.py >> autoReplyMobile &