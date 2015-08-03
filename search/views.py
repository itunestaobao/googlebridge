#!/usr/bin/python
#-*- coding: utf-8 -*-
from urllib import quote
from bs4 import BeautifulSoup
import urllib2, re, urllib, time, datetime, gzip, StringIO
from django.template import Context,loader
from django.http import HttpResponse
from wiki.models import wiki_post
from search.models import fb_words
from search.models import search_data
def index(request):
    template = loader.get_template('search/google.html')
    keywords = request.GET.get('q','').encode('utf-8')
    start_page = request.GET.get('start','0').encode('utf-8')
    

    #获取用户信息
    user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')
    user_ip = request.META.get('REMOTE_ADDR', 'unknown')
    user_referer = request.META.get('HTTP_REFERER', '直接访问')
    user_keyword = request.META.get('QUERY_STRING', 'unknown')
    nowTime=time.localtime()
    nowDate=datetime.datetime(nowTime[0],nowTime[1],nowTime[2],nowTime[3],nowTime[4],nowTime[5])
    user_keyword1 = re.split(r'&start',user_keyword)
    user_keyword2 = re.split(r'q=',user_keyword1[0])
    user_keyword3 = user_keyword2[1]
    user_keyword4 = urllib.unquote(user_keyword3)
    user_keyword5 = user_keyword4
    #敏感关键词过滤
    fb_posts = fb_words.objects.all()
    for fb_post in fb_posts:
        if re.search(fb_post.fb_word,request.GET.get('q','')):
            user_keyword4 = '中华人民共和国宪法'
        
    p1 = wiki_post(wiki_user_ip=user_ip, wiki_user_agent=user_agent, wiki_user_hostname=user_keyword5, wiki_user_referer=user_referer, timesamp=nowDate)
    p1.save()
    #i = 0
    if start_page:
        url='http://www.google.com/search?hl=zh-CN&q=%s&start=%s' % (quote(user_keyword4),quote(start_page))
    else:
        url='http://www.google.com/search?hl=zh-CN&q=%s' % quote(user_keyword4)
        start_page = 0
    #url='https://www.google.com/search?q=%s&start=%s' % (quote(keywords),quote(start_page))
    num_f = int(start_page)
    if num_f == 0:
        footnum = [1,2,3,4,5,6,7,8,9,10]

    else:
        footnum = foot_num(page(num_f))

    if search_data.objects.filter(sd_keyword__iexact=user_keyword5).filter(sd_start__iexact=start_page):
        search_data_posts = search_data.objects.filter(sd_keyword__iexact=user_keyword5).filter(sd_start__iexact=start_page)
    else:
        req = urllib2.Request(url)
        req.add_header('User-agent', 'Mozilla/5.0 (X11; Linux x86_64)')
        req.add_header('accept-encoding', 'gzip')
        req.add_header('referer', 'https://www.google.com/')

        res = urllib2.urlopen(req)
        html = res.read()
        if(res.headers.get('content-encoding', None) == 'gzip'):
            html1 = StringIO.StringIO(html)
            html_gzip = gzip.GzipFile(fileobj=html1)
            html = html_gzip.read()
            html_gzip.close()
        soup = BeautifulSoup(html)

        k = 0

        for soup1 in soup.find_all('li'):
            soup1_li = re.search(r'<li class="g">', str(soup1))
            if soup1_li:
                for link in soup1.find_all('h3'):
                    title_link=link.next.get('href')
                    if title_link:
                        url_match = re.split(r'&sa',title_link)#切割&sa
                        url_search=re.split(r'=', url_match[0])#去除等号之前的内容
                        myurl = url_search[1]
                        myurl1 = re.sub(r'%25', '%', str(myurl))
                        myurl2 = re.sub(r'%3F', '?', myurl1)
                        myurl3 = re.sub(r'%2B', '+', myurl2)
                        myurl4 = re.sub(r'%3D', '=', myurl3)
                        myurl5 = re.sub(r'%26', '&', myurl4)     
                        url_list1 = myurl5
                        url_list = url_list1[0:63]
                    else:
                        url_list='error'
                    title=re.split(r'">',str(link))
                    title1=re.split(r'</h3>',str(title[2]))
                    title_list = title1[0]


                for link1 in soup1.find_all('span'):
                    content_span = re.search(r'<span class="st">', str(link1))
                    if content_span:
                        content_list = link1
                    else:
                        content_list = '...'
                k = k + 1
                #爬取的数据放进数据库
                data_url = re.split(r'://',url_list)
                if data_url[0]=='http' or data_url[0]=='https':
                    if not search_data.objects.filter(sd_keyword__iexact=user_keyword5).filter(sd_start__iexact=start_page).filter(sd_count=k):
                        p2 = search_data(sd_keyword=user_keyword5, sd_start=start_page, sd_title=title_list, sd_url=url_list, sd_content=content_list, sd_count=k, sd_timesamp=nowDate)
                        p2.save() 
        #从search_data读取数据进行渲染显示
        search_data_posts = search_data.objects.filter(sd_keyword__iexact=user_keyword5).filter(sd_start__iexact=start_page)

    context = Context({
              'search_data':search_data_posts, 

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


