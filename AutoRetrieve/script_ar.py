import requests
import time
def write1():
   var="file.json"
   k=open(var)
   from bs4 import BeautifulSoup
   r = requests.get('http://123hindijokes.com/very-funny-jokes')
   soup = BeautifulSoup(r.content, "lxml")
   x = soup.find_all("li",limit=1)
   k.write(x)
time.sleep(2)
write1()
