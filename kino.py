import requests
from bs4 import BeautifulSoup

url = "http://kino.kz/cinema.asp?cinemaid=119"
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
info = soup.select("div.detail_content table")[1]
rows  = info.select("tr")[::1]
for row in rows:
	address = row.select("td")[0]
	name = address.select("strong a") 
	time = row.select("td:nth-of-type(1) table tbody tr")
	print("%s\t%s" % (name, time))