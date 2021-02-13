import urllib.request as url_request
from bs4 import BeautifulSoup as bs



url = "http://jkanime.net"
websiteHTML = url_request.urlopen(url).read()
soup = bs(websiteHTML, "html.parser")
#headers = soup.find_all('h2', {})

print(soup)