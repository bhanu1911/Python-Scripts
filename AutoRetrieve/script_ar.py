import codecs
import random
i=0
lis = {}
import requests
import time
from bs4 import BeautifulSoup

for j in range (1,12):
   time.
    url="http://123hindijokes.com/very-funny-jokes/"+str(j)
    r=requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    uls=soup.findAll('ul',{'class':'statusList'})
    for ul in uls:
        for li in ul.findAll('li'):
            lis[i]= li.get_text()
            i=i+1
  
with open('a.json', 'w', encoding='utf-8') as outfile:
        outfile.write(json.dumps(lis, ensure_ascii=False,indent = 4))

