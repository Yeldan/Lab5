import requests
from bs4 import BeautifulSoup

url = "http://helios.kz/toplivo/tseny-na-benzin/"
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
li = soup.select("#petroil-prices li")[0]
name = li.select("span.name")[0].text
rate = float(li.select("span.value")[0].text.replace(",", "."))
print("%s\t%f" % (name, rate))
