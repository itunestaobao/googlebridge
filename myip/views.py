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
    start_page = request.GET.get('start','0').encode('utf-8')
    i = 0
    if start_page:
        url='https://www.google.com/search?hl=zh-CN&q=%s&start=%s' % (quote(keywords),quote(start_page))
    else:
        url='https://www.google.com/search?hl=zh-CN&q=%s' % quote(keywords)
        start_page = 0
    #url='https://www.google.com/search?q=%s&start=%s' % (quote(keywords),quote(start_page))
    req = urllib2.Request(url)
    req.add_header('User-agent', 'Mozilla 5.10')
    res = urllib2.urlopen(req)
    html = res.read()
    soup = BeautifulSoup(html)
    num_f = int(start_page)
    if num_f == 0:
        footnum = [1,2,3,4,5,6,7,8,9,10]

    else:
        footnum = foot_num(page(num_f))

    k = 0
    j = 0

    titlelist=['正在加载','正在加载','正在加载','正在加载','正在加载','正在加载','正在加载','正在加载','正在加载','正在加载']
    urllist=['......','......','......','......','......','......','......','......','......','......']
    contentlist=['缓冲中...','缓冲中...','缓冲中...','缓冲中...','缓冲中...','缓冲中...','缓冲中...','缓冲中...','缓冲中...','缓冲中...']
    for soup1 in soup.find_all('li'):
        soup1_li = re.search(r'<li class="g">', str(soup1))
        if soup1_li:
            for link in soup1.find_all('h3'):
                title_link=link.next.get('href')
                url_match = re.split(r'&sa',title_link)#切割&sa
                #url_match1 = re.split(r'%',url_match[0])
                url_search=re.split(r'=', url_match[0])#去除等号之前的内容
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
              'content9':str(contentlist[9]),
              'page1':footnum[0],
              'page2':footnum[1],
              'page3':footnum[2],
              'page4':footnum[3],
              'page5':footnum[4],
              'page6':footnum[5],
              'page7':footnum[6],
              'page8':footnum[7],
              'page9':footnum[8],
              'page10':footnum[9],
              'start1':page_num(footnum[0]),
              'start2':page_num(footnum[1]),
              'start3':page_num(footnum[2]),
              'start4':page_num(footnum[3]),
              'start5':page_num(footnum[4]),
              'start6':page_num(footnum[5]),
              'start7':page_num(footnum[6]),
              'start8':page_num(footnum[7]),
              'start9':page_num(footnum[8]),
              'start10':page_num(footnum[9]),
              'keyword':keywords
         
    })
    
    return HttpResponse(template.render(context))
def page_num(num):#start canshu
    return (num-1)*10
def page(start_num):#pagenumber
    return start_num/10+1
def foot_num(num):#foot link
    if num ==1 or num ==2 or num == 3 or num == 4 or num == 5:
        return [1,2,3,4,5,6,7,8,9,10]
    return [num-5,num-4,num-3,num-2,num-1,num,num+1,num+2,num+3,num+4]


