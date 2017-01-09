import urllib
import time

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

#stockItem = '005930'
stockItem = '060250'


url = 'http://finance.naver.com/item/sise_day.nhn?code=' + stockItem
html = urlopen(url)
source = BeautifulSoup(html.read(), "html.parser")

##변수 선언
a = []
b = []
c = []

maxPage = source.find_all("table", align="center")
mp = maxPage[0].find_all("td", class_="pgRR")

mpNum = 10
#mpNum = int(mp[0].a.get('href')[-3:])

for page in range(1, mpNum + 1):
    print(str(page))
    url = 'http://finance.naver.com/item/sise_day.nhn?code=' + stockItem + '&page=' + str(page)
    html = urlopen(url)
    source = BeautifulSoup(html.read(), "html.parser")
    srlists = source.find_all("tr")
    isCheckNone = None

    ##if ((page % 1) == 0):
    ##    time.sleep(1.50)

    for i in range(1, len(srlists) - 1):
        if (srlists[i].span != isCheckNone):
            srlists[i].td.text
            print(srlists[i].find_all("td", align="center")[0].text, srlists[i].find_all("td", class_="num")[0].text, srlists[i].find_all("span",class_="tah p11")[4].text)
            a.append(srlists[i].find_all("td", align="center")[0].text)
            #b.append(srlists[i].find_all("td", class_="num")[0].text)
            b.append(srlists[i].find_all("td", class_="num")[0].text.replace(',',''))
            c.append(srlists[i].find_all("span",class_="tah p11")[4].text.replace(',',''))


d = {'Name':b, 'Volume':c}
df1 = pd.DataFrame(d, index=a)


df2 = pd.to_numeric(df1.Name)
df3 = pd.to_numeric(df1.Volume)

df = pd.concat([df2, df3], axis=1, join_axes=[df2.index])
df = df.iloc[::-1]

df.to_csv('Stock.csv')
