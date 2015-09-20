#! -*- coding:utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup as bs

base_url = "https://getpocket.com/"

headers = {"Content-Type":"text/html","User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36"}

s = requests.Session()

s_get = s.get(base_url,headers=headers)

#for k in s_get.cookies:
#    print k
#print s_get.cookies.keys()

form_check = re.findall(r'name="form_check" value="(\S+)"',s_get.text, re.S)

print form_check

data = {"form_check":form_check,"feed_id":'youremail',"password":'yourpasswod',"route":'',"source":"email","source_page":"/","is_ajax":1}

login_url = base_url + "login_process.php"

s_post = s.post(login_url, data)

headers = {
'Host':'getpocket.com',
'Connection':'keep-alive',
'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
'Accept-Encoding':'gzip,deflate,sdch',
'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4,de;q=0.2'
}
list_url = "http://getpocket.com/a/"
s_getlist = s.get(list_url, headers=headers)

formCheck = re.findall(r"var formCheck = '(\S+)';", s_getlist.text, re.S)

print formCheck

list_post_data = {
'offset':0,
'count':30,
'state':'queue',
'favorite':'',
'sort':'newest',
'search':'',
'tag':'',
'view':'list',
'appsInfo':'summary',
'forcegroups':1,
'formCheck':formCheck
}

list_url = "http://getpocket.com/a/x/get.php"
list_post = s.post(list_url, data=list_post_data, headers=headers)


co = '''

#login_url = base_url + "login_process/"
#login_url = base_url + "web/x/pv.php"
login_url = base_url
#login_url = base_url + "login.php"

p_post = requests.post(login_url, data)

Cookies = p_post.cookies

get_url = "http://getpocket.com/a/queue/list/"

p_get = requests.get(get_url, cookies=Cookies)
'''
f = open('pocketpage.html','w')
f.write(list_post.text.encode('utf8'))
print list_post.text.decode('gb2312')
f.close()


print "Done"

