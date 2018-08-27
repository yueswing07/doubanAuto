# -*- coding: utf-8 -*-

class Cookie(object):
    """docstring for Cookie"""
    def __init__(self, arg,type=0):
        super(Cookie, self).__init__()

        self.cookiesDit = {}
        self.parse(arg,type)
        
    def set(self,key,value):
        self.cookiesDit[key] = value

    def get(self,key):
        try:
            return self.cookiesDit[key]
        except Exception:
            return ''
    def getAll(self):
            return self.cookiesDit
    def remove(self,key):
        try:
            del self.cookiesDit[key]
        except Exception:
            return ''

    # strOrFilename string(type=0) or filename(type=1) 
    def parse(self,strOrFilename,type=0):
        cookies = {}
        if 0==type:
            douban_cookies =strOrFilename.split("; ")
            for line in douban_cookies:
                key, value = line.split("=", 1)
                cookies[key] = value
        elif 1==type:
            with open(strOrFilename, "r") as f_cookie:
                douban_cookies = f_cookie.readlines()[0].split("; ")
                for line in douban_cookies:
                    key, value = line.split("=", 1)
                    cookies[key] = value
        # print(cookies)
        self.cookiesDit =  cookies
            # return cookies
            
if __name__ == "__main__":
    cookiesStr = 'bid=ZneGZ9dF008; ll="108288"; _ga=GA1.2.509933802.1529456369; __yadk_uid=7KhWXonEVAUOamdRoD13vwz0nwAUdglp; ap=1; _vwo_uuid_v2=D7203DB0D34A627D8C0CD470DECF6EA94|1eeacdeabfa10beda79f08e1753db37b; gr_user_id=5f3e7fc5-8dcf-48d1-968e-bc171bfd66f3; ck=LISO; douban-fav-remind=1; douban-profile-remind=1; __utmc=30149280; __utmv=30149280.16660; __utmz=30149280.1531553870.3.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ps=y; session=VGn4SE69ID1kNOsT_C2AHoAFOBCXYUEesy7IphEjQwQ7b5UsvliHiZlJmTd3Xa4aU_FhQSMClzRDEcVMeDUGyIACSohjU1tHQdbU2OIUFK19cQFVBXN0YXRlcQJVCng3OGNVMjFSRDVxA3OHcQQu; ct=y; push_doumail_num=0; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1532512334%2C%22https%3A%2F%2Fmusic.douban.com%2Fsubject%2F30166746%2F%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.509933802.1529456369.1532502344.1532512335.61; __utmb=30149280.500.4.1532516951574; push_noty_num=0; _pk_id.100001.8cb4=eb21927d75c14542.1529456368.171.1532524086.1532504023."'
    cookie = Cookie(cookiesStr)
    print(cookie)
    print(cookie.cookiesDit)
    # for x in cookie.cookiesDit:
    #     print(x)
    print(cookie.get('bid'))
    cookie.set('bidd','aa')
    print(cookie.get('bidd',))
