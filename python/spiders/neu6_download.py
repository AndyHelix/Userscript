# - *- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs
import re

posturl = "http://bt.neu6.edu.cn/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes"

data = {"username":'Ú¤ÍõÐÇÖ®Ò¹',"password":'15120092341lxy'}

rpost = requests.post(posturl, data)
Cookies = rpost.cookies

#geturl = "http://bt.neu6.edu.cn/forum.php"
geturl = "http://bt.neu6.edu.cn/forum-13-1.html"

rget =  requests.get(geturl,cookies=Cookies)

f = open('webpage.html','w')
f.write(rget.text.encode('utf8'))
f.close()

soup = bs(rget.text)
#print rget.text[0:100]
p = re.compile(r'id="normalthread_\d+"')
#search = p.search(rget.text)
find = p.findall(rget.text)
#print find[2],"\n",len(find),find[-1]
#for i in find:
i = find[-1]
#print i
id_s = i[4:-1]
#print id_s
#print soup.find_all(id=id_s)

string = '''
p_url = re.compile(r'href="thread\-14\d+\-1\-1.html"', re.S)
f_url = p_url.findall(rget.text)
for d_url in range(0,len(f_url)):
    if d_url%2:
        dl_url = d_url[6:-2]
        d_get = requests.get("http://bt.neu6.edu.cn/"+dl_url, cookies=Cookies)

'''
base_url = "http://bt.neu6.edu.cn/"
#dl = "http://bt.neu6.edu.cn/forum.php?mod=attachment&aid=NDU1MTUzMHxhNTcxNWQwZnwxNDEyNjgzMjQxfDY0MzcwfDE0MDU4MDI%3D"
#dl = "http://bt.neu6.edu.cn/forum.php?mod=attachment&aid=NDU1MTUzMHw5NjEwZmJlYXwxNDEyNjg0MDE0fDY0MzcwfDE0MDU4MDI%3D&ck=124e1fac"
dl = "http://bt.neu6.edu.cn/thread-1405943-1-1.html"
r = requests.get(dl, cookies=Cookies)
dl_p = re.compile(r'<a href="forum.php\?mod=attachment&amp;aid=.*"')
dl_s = dl_p.findall(r.text)[-1]
print dl_s.split()[1][6:-1]
print re.sub("amp;","",dl_s.split()[1][6:-1])
dl_url = re.sub("amp;","",dl_s.split()[1][6:-1])
lasturl = "http://bt.neu6.edu.cn/"+ dl_url
print lasturl
r = requests.get(lasturl, cookies=Cookies)
last_p = re.compile(r'<a href="forum.php\?mod=attachment&aid=.*"')
last_s = last_p.search(r.text)
print last_s.group().split('"')[1]
ut_url = base_url + last_s.group().split('"')[1]

r = requests.get(ut_url, cookies=Cookies)
with open("name.torrent",'wb') as ut:
    ut.write(r.content)
    print "Download Done"

    
#print len(soup.find_all("a",href=re.compile("thread")))

#s = soup.find_all("tbody", id=re.compile('nor'))[0]
#s = soup.find_all("tbody", id=re.compile(r'normalthread_\d+'))[0]

# print (s)


