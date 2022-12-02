import requests
from bs4 import BeautifulSoup

pdfPageLink = []
downloadLinks = []

URL = "https://riptutorial.com/ebook"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

for book in soup.select('#uiTagResult > li'):
  pdfPageLink.append("https://riptutorial.com/ebook" + book.find("a").get('href'))

for pageLink in pdfPageLink:
  URL = pageLink
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  #downloadLinks.append(soup.find(".container-chapters > a"))
  print(soup.find("div", {"class": "container-chapters"}).find('a').get('href'))
  

#print(downloadLinks)