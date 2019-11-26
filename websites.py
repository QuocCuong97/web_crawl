import re
import requests
import urllib.request
from bs4 import BeautifulSoup
from objects import ObjectCrawl
from json_execute import export_to_json


class NewsCloud365(object):

    def __init__(self):
        self.url = "https://news.cloud365.vn/"
        self.source = "Cloud365"

    def get_dom(self, val):
        self.page_id = val
        page = urllib.request.urlopen(self.url + 'page/{}'.format(self.page_id))
        dom = BeautifulSoup(page, 'html5lib')
        return dom

    def get_objects(self):
        try:
            start_page = 1
            list_objects = []
            while True:
                html_dom = self.get_dom(start_page)
                mark = html_dom.findAll(class_="post-header")
                for x in mark:
                    title_search = x.find(['a', "href"])
                    self.title = title_search.string

                    link_search = x.find(['a', "href"])
                    self.link = link_search['href']

                    time_search = x.find(attrs={'class' : 'post-date'})
                    self.time = time_search.string

                    author_search = x.find(attrs={'class' : 'post-author'})
                    self.author = author_search.string
                
                    new_post = ObjectCrawl(self.title, self.link, self.time, self.author, self.source)
                    dic = new_post.to_dict()
                    list_objects.append(dic)
                start_page+=1
        except:
            pass
        return list_objects

class TecAdmin(NewsCloud365):

    def __init__(self):
        self.url = 'https://tecadmin.net/'
        self.source = 'TecAdmin'

    def get_objects(self):
        try:
            start_page = 1
            list_objects = []
            while start_page <= 10:
                html_dom = self.get_dom(start_page)
                mark = html_dom.findAll(class_="post-box")
                for x in mark:
                    title_search = x.find(['a', "href"])
                    self.title = title_search.string

                    link_search = x.find(['a', "href"])
                    self.link = link_search['href']

                    time_search = x.find(attrs={'class' : 'updated'})
                    self.time = time_search['datetime']

                    author_search = x.find(attrs={'class' : 'fn'})
                    self.author = author_search.string
                
                    new_post = ObjectCrawl(self.title, self.link, self.time, self.author, self.source)
                    dic = new_post.to_dict()
                    list_objects.append(dic)
                start_page+=1
        except:
            pass
        return list_objects


class Techrum(object):

    def __init__(self):
        self.url = 'https://www.techrum.vn/articles/'
        self.homepage = 'https://www.techrum.vn'
        self.source = 'Techrum'

    def get_dom(self, val):
        self.page_id = val
        page = urllib.request.urlopen(self.url + 'page-{}'.format(self.page_id))
        dom = BeautifulSoup(page, 'html5lib')
        return dom

    def get_objects(self):
        try:
            start_page = 1
            list_objects = []
            while start_page <= 5:
                html_dom = self.get_dom(start_page)
                mark = html_dom.findAll(class_="porta-article-item")
                for x in mark:
                    title_search = x.find(['a', "href"])
                    self.title = title_search.string
                    self.title = self.title.strip()

                    link_search = x.find(['a', "href"])
                    self.link = link_search['href']
                    self.link = self.homepage + self.link

                    time_search = x.find(attrs={'class' : 'u-dt'})
                    self.time = time_search['data-date-string']

                    author_search = x.find(attrs={'class' : 'u-concealed'})
                    self.author = author_search.string
                    self.author = self.author.strip()
                
                    new_post = ObjectCrawl(self.title, self.link, self.time, self.author, self.source)
                    dic = new_post.to_dict()
                    list_objects.append(dic)
                start_page+=1
        except:
            pass
        return list_objects


class DigitalOcean(object):

    def __init__(self):
        self.url = "https://www.digitalocean.com/community/tutorials"
        self.homepage = "https://www.digitalocean.com/community/"
        self.source = "DigitalOcean"
    
    def get_objects(self):
        list_objects = []
        page = requests.get(self.url)
        html_dom = BeautifulSoup(page.text, 'html5lib')
        mark = html_dom.findAll(attrs={'class' : 'feedable-details'})
        for x in mark:
            title_search = x.find('h3')
            self.title = title_search.string.strip()
                    
            link_search = x.find("a", {"data-js": True})
            self.link = self.homepage + link_search['href']

            time_search = x.find(attrs={'class' : 'publish-date timeago'})
            self.time = time_search['title']
            
            author_search = x.find(attrs={'class' : 'authors'})
            self.author = author_search.string.strip()
            self.author = re.sub('By', '', self.author)
            self.author = self.author.strip()

            new_post = ObjectCrawl(self.title, self.link, self.time, self.author, self.source)
            dic = new_post.to_dict()
            list_objects.append(dic)
        return list_objects


class CuongQuach(NewsCloud365):

    def __init__(self):
        self.url = "https://cuongquach.com/category/linux/"
        self.source = "CuongQuach"

    def get_objects(self):
        try:
            start_page = 1
            list_objects = []
            while True:
                html_dom = self.get_dom(start_page)
                mark = html_dom.findAll(class_="td-block-span6")
                for x in mark:
                    title_search = x.find(attrs={'class' : 'entry-title td-module-title'})
                    title_search = title_search.a
                    self.title = title_search['title']

                    self.link = title_search['href']

                    time_search = x.find(attrs={'class' : 'entry-date updated td-module-date'})
                    self.time = time_search.string

                    author_search = x.find(attrs={'class' : 'td-post-author-name'})
                    author_search = author_search.a
                    self.author = author_search.string
                    
                    new_post = ObjectCrawl(self.title, self.link, self.time, self.author, self.source)
                    dic = new_post.to_dict()
                    list_objects.append(dic)
                start_page+=1
        except:
            pass
        return list_objects