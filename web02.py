#web02.py

import urllib.request
from bs4 import BeautifulSoup

#file
#page= open("https://justdoitproject.tistory.com/15",'rt',encoding='utf-8').read()
page= urllib.request.urlopen("https://justdoitproject.tistory.com/15")

#soup 객체 생성
soup = BeautifulSoup(page,'html.parser')

#tag검색
print(soup.prettify())

print(soup.find_all('p'))

print(soup.find('p'))

print(soup.find_all('p',class_=''))
print(soup.find_all(id='first'))
#print(soup.find_all('p').get_text()) #error occur
print(soup.find('p').get_text())

for tag in soup.find_all('p'):
    print(tag.get_text())
