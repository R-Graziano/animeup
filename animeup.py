import urllib.request as url_request
from bs4 import BeautifulSoup as bs

def myfunct(anime):
    if anime in new_episodes_list:
        return True
    else:
        return False

class Anime(object):
    episodes = []
    status = ""

    def __init__(self, name, status="watching"):
        self.name = name
        self.status = status
    
    def add_episode(self, episode_number):
        self.episodes.append(episode_number)

    def status_watching(self):
        self.status = "watching"

    def status_end(self):
        self.status = "ended"

    def status_pending(self):
        self.status = "pending"


# Url request and get data
url = 'http://jkanime.net'
visitor = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201"}
request = url_request.Request(url,None,visitor)
websiteHTML = url_request.urlopen(request).read()
soup = bs(websiteHTML, 'html.parser')
headers = soup.find_all('a', {'class':"odd", 'rel':"bookmark"})

new_episodes_list = []

for new_episode in headers:
    episode_name = new_episode['title']
    episode_number = new_episode['href'].split('/')[4]
    episode_link = new_episode['href']
    print("{:50} - {:3} {:50}".format(episode_name,episode_number,episode_link))
    new_episodes_list.append(new_episode['title'])

#print("\n{}".format(new_episodes_list), end="\n\n")

# Animes that I follow
myAnimeList = ["Beastars 2nd Season","Re:Zero kara Hajimeru Isekai Seikatsu 2nd Season Part 2","Dr. Stone: Stone Wars",
                "Kumo Desu ga, Nani Ka?","Jujutsu Kaisen (TV)","Shingeki no Kyojin: The Final Season","Log Horizon: Entaku Houkai",
                "Tensei shitara Slime Datta Ken 2nd Season","Yakusoku no Neverland 2nd Season",
                "Tatoeba Last Dungeon Mae no Mura no Shounen ga Joban no Machi de Kurasu Youna Monogatari",
                "Kimetsu no Yaiba Movie: Mugen Ressha-hen"]

news = list(filter(myfunct,myAnimeList))
print("\n{}".format(news))