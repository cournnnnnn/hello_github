import requests
from bs4 import BeautifulSoup4


url = 'www.baidu.com'
res = requests.get(utl)
html = res.text


print(html)
