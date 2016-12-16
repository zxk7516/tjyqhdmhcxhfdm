from urllib.request import urlopen
from bs4 import BeautifulSoup
def print_source(html):
    print(html.read())
html = urlopen('http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2015/index.html')
bsObj = BeautifulSoup(html.read(),'html.parser')
provincetable = bsObj.select('table.provincetable a')

