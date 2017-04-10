import requests
import time
from bs4 import BeautifulSoup
def write1():
   var="file.json"
   k=open(var)
   r = requests.get('http://123hindijokes.com/very-funny-jokes')
   soup = BeautifulSoup(r.content, "lxml")
   x = soup.find_all("li",limit=1)
   k.write(x)
time.sleep(1000)
write1()
