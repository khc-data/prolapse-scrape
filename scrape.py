#!/usr/bin/env python3
from bs4 import BeautifulSoup
import urllib.request

urlToScrape = 'https://www.etfchannel.com/finder/?a=etfsholding&symbol=GME'
req = urllib.request.Request(urlToScrape, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest", "Cookie": "__utmc=40499190; __utmz=40499190.1621622240.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not provided); __gads=ID=3641c960186af6b0-226a27b51bc8004a:T=1621622240:S=ALNI_Mb20GvU-bNBFs5RVE-_lD8lYJ-f0w; _ga=GA1.2.1380513312.1621622239; _gid=GA1.2.324686984.1621622240; __qca=P0-1616499648-1621622239950; slogin=1621622706; slogin=1621622706; coregval=ims; __utma=40499190.1380513312.1621622239.1621622239.1621625040.2"})
with urllib.request.urlopen(req) as response:
    targetContent = response.read()
targetObject = BeautifulSoup(targetContent, 'html.parser')
table = targetObject.find_all("table", attrs ={"border":"0", "width": "100%", "cellpadding":"0", "cellpadding":"0"})
tds = table[1].find_all('td')

result = {}

i=0
for cells in tds:
    if i%3 == 0:
        resultName = str(tds[i].font.a.string).strip()
    if i%3 == 2:
        resultValue = str(tds[i].font.string).strip()
        result.update({resultName : resultValue})
    i=i+1

for x, y in result.items():
    print(x, y)
