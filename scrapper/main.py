import requests
from bs4 import BeautifulSoup

pdfPageLink = []

URL = "https://www.pdfdrive.com/a-level-books.html"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

for pageLink in soup.select('.files-new > ul > li'):
  pdfPageLink.append(pageLink.find("a").get('href'))

print(pdfPageLink)