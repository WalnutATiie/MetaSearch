from engines.sogouFactory import SogouFactory
from query.query_engines import AccessUrls
from engines.youdaoFactory import YoudaoFactory
import sys
query = sys.argv[1]
youdao = YoudaoFactory()#test
youdao_urls = youdao.urlGenerator(query)
sogou = SogouFactory()
sogou_urls = sogou.urlGenerator(query)
a = AccessUrls()
a.gtaskManager(youdao_urls,youdao.extractSearchResults,proxy_flag = 0,ua_flag = 1)
a.gtaskManager(sogou_urls,sogou.extractSearchResults,proxy_flag = 0,ua_flag = 1)
