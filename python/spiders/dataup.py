#!/usr/bin/env python
# encoding: utf-8
# author: andyhelix
# email: alayasix@foxmail.com
  
import requests
import re
import os
import time

# 传入参数 背景 background.txt go列表 golist.txt gopath

def runurl(reffile, probefile, resultpath):
    url = "http://omicslab.genetics.ac.cn/GOEAST/php/process_customized.php"

    targetpath = resultpath

    s = requests.Session()

    dataload = {'email':'1005534145@qq.com','graph_type':'png'}
    datafiles = {'annotation_file':(reffile,open(reffile,'r'),'text/plain'),'customized_probe_file':(probefile,open(probefile,'r'),'text/plain')}

    r = s.post(url, data=dataload, files=datafiles)

    done = "<h3>All process complete successfully!</h3>"
    p = re.compile(done)
    pre = p.search(r.text).group()
    print pre
    if pre:
        # 获取query time
        timep = re.compile(r"value='(\d+.\d+)'")
        timere = timep.search(r.text).group(1)
        queryvalue = timere
# 再次 post
        posturl_2 = "http://omicslab.genetics.ac.cn/GOEAST/php/show_customized.php"
        dataload_2 = {'query_time': queryvalue, 'graph_type':'png', 'job_name':''}
        r_2 = s.post(posturl_2, data=dataload_2)

        with open('content_2.html','w') as f:
            f.write(r_2.text)
            f.close()
        # 下载结果
        dpath = 'refile19.txt'
        bpath = 'bp.png'
        cpath = 'cc.png'
        mpath = 'mf.png'

        detailurl = "http://omicslab.genetics.ac.cn/GOEAST/download/result_-"+queryvalue+'.txt'
        bpurl = "http://omicslab.genetics.ac.cn/GOEAST/download/BP_-"+queryvalue+'.png'
        ccurl = "http://omicslab.genetics.ac.cn/GOEAST/download/CC_-"+queryvalue+'.png'
        mfurl = "http://omicslab.genetics.ac.cn/GOEAST/download/MF_-"+queryvalue+'.png'
        urldict = {'re':detailurl,'bp':bpurl,'cc':ccurl,'mf':mfurl}
        def setfilename(downloadurl, targetpath):
            newdict = {}
            for k in downloadurl:
                newdict[k] = targetpath+os.path.sep+downloadurl[k].split('/')[-1]
            return newdict
        pathdict = setfilename(urldict, targetpath)
        savefile(urldict, pathdict, s)
    else:
        print "Server or updata error"

def savefile(urldict, pathdict, s):
    for k in urldict:
        r = s.get(urldict[k])
        with open(pathdict[k],'wb') as f:
            f.write(r.content)

def applytopath(reffile, mainpath):

    ref = reffile
    n = 0

    for r, dirs, files in os.walk(mainpath):
        if len(r.split(os.path.sep)) == 15:
            for f in files:
                if f.startswith('go'):
                    if os.path.getsize(r+os.path.sep+f)>10:
                        gofile = r+os.path.sep+f
                        n += 1
                        print n
                        runurl(ref, gofile, r)
                        print 'DONE'+'*'*20
                    else:
                        print 'Fail'+'*'*20
                        print f
                        print 'less than 10b'
                else:
                    print f
                    print 'something wrong'
                time.sleep(5)

if __name__ == '__main__':
    import time
    start = time.time()
    mainpath = '/disk/fate/python/data_analysis/pandas/rnadata/allgoresult/gosum/goeast/newdir'
    reffile = 'background.txt'

    applytopath(reffile, mainpath)

    end = time.time()
    print end - start
