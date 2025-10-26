import threading
import requests
import bs4
from bs4 import BeautifulSoup
urls=['https://www.wikipedia.org/','https://www.icc-cricket.com/tournaments/womens-cricket-worldcup-2025']
def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(len(soup.text))
content=[]
for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url))
    content.append(thread)
    thread.start()
for thread in content:
    thread.join()
print(content)
print("allweb are read")
        