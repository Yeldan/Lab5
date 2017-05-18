import requests
from bs4 import BeautifulSoup

url = "http://www.nationalbank.kz/?furl=cursFull&switch=rus"
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
tr = soup.select("table.gen4 tr")[11]
name = tr.select("td.gen7")[0].text
rate = float(tr.select("td.gen7")[2].text.replace(",", "."))
print("%s\t%f" % (name, rate))

