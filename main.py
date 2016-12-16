from urllib.request import urlopen
from bs4 import BeautifulSoup
def print_source(html):
    print(html.read())
def doExplore(a='index.html',tableclass = 'provincetable'):
    print(a+'....')
    html = urlopen('http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2015/'+a)
    bsObj = BeautifulSoup(html,'html.parser')
    current_table =  bsObj.select('table.'+tableclass+' a')
    for a in current_table:
        print(a.text)



html = urlopen('http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2015/index.html')
bsObj = BeautifulSoup(html.read(),'html.parser')
provincetable = bsObj.select('table.provincetable a')
# print(provincetable)
for a in provincetable:
    # print(type(a))
    print('解析'+a.text);
    doExplore(a.attrs.get('href'),'citytable')
    # ad =  BeautifulSoup(a,'html.parser')
    # print(ad.text)
    # print(ad.attrs('href'))
