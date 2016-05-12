#!/usr/bin/env python
# encoding: utf-8
from enginesFactory import EngineFactory
from bs4 import BeautifulSoup
import logging
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re
import random
import types
import os
from searchResult import SearchResult
class YoudaoFactory(EngineFactory):
    def __init__(self):
        self.engine_name = "youdao"
        self.engine_domain = "http://www.youdao.com/"
        self.weight = 5
        self.results_num = 100
        self.page_num = 10
        self.results_per_page = 10
    def urlGenerator(self,query):
        urls_list = list()
        try:
            assert self.page_num > 0 and self.results_num > 0
        except AssertionError:
            logging.error(
                'Parameter error,please check the parameters.Program Aborted')
        else:
            urls = list()
            for p in range(1, self.page_num+1):
                #url = self.engine_domain+"web?query="+query+"&page="+str(p)+"&ie=utf8"
                start = (p-1)*self.results_per_page
                url = self.engine_domain+"search?q="+query+"&start="+str(start)+"&ue=utf8&keyfrom=web.page"+str(p)+"&lq="+query+"&timesort=0"
                urls_list.append(url)
        return urls_list
    def extractSearchResults(self,html,url):
        search_results = list()
        soup = BeautifulSoup(html)
        try:
            ol = soup.find_all('ol',id='results')
            lis = ol[0].children

        except:
            logging.error("fail to extract the page:%s",url )
        else:
            for li in lis:
                search_result = SearchResult()
                try:
                    search_result.setURL(li.find('a')['href'])
                except:
                    search_result.setURL("")
                try:
                    search_result.setContent(li.find('p').text)
                except:
                    search_result.setContent("")
                try:
                    search_result.setTitle(li.find('a').text)
                except:
                    search_result.setTitle("")
                if search_result.getURL() != "":
                    search_result.printIt()
                    search_results.append(search_result)
            return search_results
