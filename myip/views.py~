#!/usr/bin/python
#-*- coding: utf-8 -*-
from urllib import quote
from bs4 import BeautifulSoup
import urllib2, re
from django.template import Context,loader
from django.http import HttpResponse

def index(request):
    template = loader.get_template('myip/google.html')
    keywords = request.GET.get('q','').encode('utf-8')
    url='https://www.google.com/search?q=%s' % quote(keywords)
    req = urllib2.Request(url)
    req.add_header('User-agent', 'Mozilla 5.10')
    res = urllib2.urlopen(req)
    html = res.read()
    soup = BeautifulSoup(html)
    k = 0
    j = 0
    i = 0
    titlelist=['正在加载','正在加载','正在加载','正在加载','正在加载','正在加载','正在加载','正在加载','正在加载','正在加载']
    urllist=['......','......','......','......','......','......','......','......','......','......']
    contentlist=['缓冲中...','缓冲中...','缓冲中...','缓冲中...','缓冲中...','缓冲中...','缓冲中...','缓冲中...','缓冲中...','缓冲中...']
    for soup1 in soup.find_all('li'):
        soup1_li = re.search(r'<li class="g">', str(soup1))
        if soup1_li:
            for link in soup1.find_all('h3'):
                title_link=link.next.get('href')
                url_match = re.split(r'&sa',title_link)
                #url_match1 = re.split(r'%',url_match[0])
                url_search=re.split(r'=', url_match[0])
                myurl = url_search[1]
                urllist[k]=myurl
                title=re.split(r'">',str(link))
                title1=re.split(r'</h3>',str(title[2]))
                titlelist[k] = title1[0]
                #k = k + 1    
            for link1 in soup1.find_all('span'):
                content_span = re.search(r'<span class="st">', str(link1))
                if content_span:
                    contentlist[k] = link1
                    #j = j + 1 
            k = k + 1
    context = Context({
              'link0':str(urllist[0]), 
              'title0':str(titlelist[0]), 
              'content0':str(contentlist[0]),  
              'link1':str(urllist[1]), 
              'title1':str(titlelist[1]), 
              'content1':str(contentlist[1]),
              'link2':str(urllist[2]), 
              'title2':str(titlelist[2]), 
              'content2':str(contentlist[2]),  
              'link3':str(urllist[3]), 
              'title3':str(titlelist[3]), 
              'content3':str(contentlist[3]),
              'link4':str(urllist[4]), 
              'title4':str(titlelist[4]), 
              'content4':str(contentlist[4]),
              'link5':str(urllist[5]), 
              'title5':str(titlelist[5]), 
              'content5':str(contentlist[5]),
              'link6':str(urllist[6]), 
              'title6':str(titlelist[6]), 
              'content6':str(contentlist[6]),
              'link7':str(urllist[7]), 
              'title7':str(titlelist[7]), 
              'content7':str(contentlist[7]),
              'link8':str(urllist[8]), 
              'title8':str(titlelist[8]), 
              'content8':str(contentlist[8]),
              'link9':str(urllist[9]), 
              'title9':str(titlelist[9]), 
              'content9':str(contentlist[9])
         
    })
    
    return HttpResponse(template.render(context))
