from bs4 import BeautifulSoup
import requests
import json
import codecs
import random
t=0
list1 = {}
print("In the mood for some jokes, are we?"
for t in range (1,12):
    url = "http://123hindijokes.com/very-funny-jokes/"+str(j)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    uls = soup.findAll('ul',{'class':'statusList'})
    for ul in uls:
        for li in ul.findAll('li'):
            list1[i]= li.get_text()
            i=i+1
with open('a.json', 'w', encoding='utf-8') as outfile:
    outfile.write(json.dumps(list1, ensure_ascii=False,indent = 4))
print("Here you go!")
