#web01
import urllib.request
from bs4 import BeautifulSoup

page= urllib.request.urlopen("https://justdoitproject.tistory.com/15")

#soup 객체 생성
soup = BeautifulSoup(page,'html.parser')

#tag검색
print(soup.find_all("title"))

