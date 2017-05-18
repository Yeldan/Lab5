import requests

session = requests.Session()
r = session.get('http://intranet2.kbtu.kz/login.aspx')
my_data = {
 'uname': 'd.esmukhanov',
 'pwd': 'Nu8920qod3'
}
r = session.post('http://intranet2.kbtu.kz/login.aspx', data = my_data)
from bs4 import BeautifulSoup
html = r.text
soup = BeautifulSoup(html, "html.parser")
titles = soup.select('#MainContent .TitleContainer .Title')
descriptions = soup.select('#MainContent .Description')
for item in titles:
 text = item.text.strip()
 print(text)