
import urllib.request
from bs4 import BeautifulSoup
data = urllib.request.urlopen('http://ksp.multicampus.com/ksp/servlet/controller.gate.common.GateConstServlet?p_grcode=SRV2366&p_ssochk=N&p_gubun=&p_ifsubj=&p_ifyear=&p_ifsubjseq=&p_ifdistcode=#')
data = urllib.request.urlopen("https://justdoitproject.tistory.com/15")

soup = BeautifulSoup(data,'html.parser')

list = soup.find_all('li')#,attrs={'class':'menu01'})

for item in list:
    print(item.get_text())
    try:
        title= item.find('a').get_text()
        print(title.strip())#공백제거
    except:
        print('no')
        pass


import re

for tag in soup.find_all('p'):
    print(tag)


    
 
