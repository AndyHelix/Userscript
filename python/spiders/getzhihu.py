#! -*- coding:utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup as bs

headers = {"Content-Type":"text/html","User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36"}
base_url = "http://www.zhihu.com/"

#login_url = base_url + "login_process/"
#login_url = base_url + "web/x/pv.php"
login_url = base_url + "login"
#login_url = base_url + "login.php"

# get xsrf
g_xsrf = requests.get(base_url)

#
#print g_xsrf.text
g_xsrf_data = g_xsrf.text

pattern_xsrf = re.compile(r'name="_xsrf" value="(.*)"', flags=0)
xsrf = pattern_xsrf.findall(g_xsrf_data)
d_xsrf = xsrf[0]
print d_xsrf

data = {"_xsrf":d_xsrf,"rememberme":'y',"email":'yssqcbq@sohu.com',"password":'3128014utc'}

s = requests.Session()

s.post(login_url, data)

headers = {"Content-Type":"text/html","User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36"}
t_url = "http://www.zhihu.com/explore/recommendations"
getdata = s.get(t_url,headers=headers)
coo = '''
#post
p_post = requests.post(login_url,data)

Cookies = p_post.cookies
print Cookies

t_url = "http://www.zhihu.com/explore/recommendations"
p_get = requests.get(t_url, cookies=Cookies)


#get_url = "http://getpocket.com/a/queue/list/"
#get_url = base_url

#p_get = requests.get(get_url, cookies=Cookies)
'''
f = open('zhihupage.html','w')
f.write(getdata.text.encode('utf8'))
f.close()

get_soup = bs(getdata.text)

items = get_soup.find_all("a", class_="question_link")

for i in items:
    print i.encode("gb2312")

print 20*"Done"
findq = re.compile(r'"question_link" href="/question/\d+/answer/\d+"',re.S)
findqs = findq.findall(getdata.text)
for i in findqs:
    print i.encode('utf8')
print "Done"
