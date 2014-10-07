#!/usr/bin/env python
# encoding: utf-8

import urllib2
from bs4 import BeautifulSoup as bs
import re

print "输入下载页数(0-47)(每页20本)"
number = raw_input()

num = int(number)

booklist = []

for i in range(0,num+1):
    target = "http://book.douban.com/tag/web?start="+str(i*20)+"&type=T"
    print target

    data = urllib2.urlopen(target).read()

    soup = bs(data)

    for item in soup.find_all("li", class_="subject-item"):
        item_str = unicode(item)
    #    print item_str
        #name = re.search(r'title="(.*)"',item_str, flags=re.S).group(1)
        #name = re.search(r'title="(.*)"',item_str).group(1)
        pattern = re.compile(r'title="(.*)"', re.X)
        match = pattern.search(item_str)
        if match:
            name = match.group(1)
        booklist.append(name)
        print name


booklist_str = "\n".join(booklist)
f = open("doubanbook.txt", 'w')
f.write(booklist_str.encode('utf-8'))
f.close()
print "Download Done"


