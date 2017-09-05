import sys
import os
import requests
from bs4 import BeautifulSoup

req = input('Input text of request. Please, separate words by sumbol \"+\"\n')
page = 1
os.makedirs('pics/' + str(req), mode=0o777, exist_ok=True)
while 1:
    url = 'https://www.zerochan.net/' + str(req) + '?p=' + str(page);
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
          }
    r = requests.get(url, headers = headers)
    soup = BeautifulSoup(r.text, "lxml")
    items = soup.find('ul', {'id': 'thumbs2'}).findAll('li')
    if not items:
        break
    print('Saving page ' + str(page) + '\n')
    for item in items:
        pic_link = item.find('p').find('a')
        if not pic_link:
            continue
        pic_link = pic_link.get('href')    
        pic_name = (item.find('a').get('href'))[1:]
        p = requests.get(pic_link)
        out = open('pics/' + str(req) + '/' + str(pic_name) + pic_link[-4:], "wb")
        out.write(p.content)
        print(str(pic_name) + ' is saved')
        out.close()
    page = page + 1
    print()
#Toujou+Nozomi
