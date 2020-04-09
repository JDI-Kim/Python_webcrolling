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

#--
# web02.py
from bs4 import BeautifulSoup
page = open('sample.html', 'rt', encoding='utf-8').read()
soup = BeautifulSoup(page, 'html.parser')
#print(soup.prettify())

#문서 내부에 있는 <p>태그를 모두 검색합니다. 
#print(soup.find_all('p'))

#<p>태그 하나만 검색합니다. 
#print(soup.find('p'))

#<p>태그 중에 class="outer-text"만 검색합니다. 
#print(soup.find_all('p', class_='outer-text'))

#태그를 지정하고 지정하지 않고 class="outer-text"인 경우를 검색합니다. 
#print(soup.find_all(class_='outer-text'))

#태그의 id속성이 id="first"인 경우를 검색합니다. 
#print(soup.find_all(id='first'))

#<p>태그를 찾아서 내부의 문자열만 출력합니다.
for tag in soup.find_all('p'):
    print(tag.get_text())

