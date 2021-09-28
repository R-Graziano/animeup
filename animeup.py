#!/usr/bin/env python
import urllib.request as url_request
from bs4 import BeautifulSoup as bs
import balloontip as bt


class Anime(object):
    name = ""
    episodes = []
    status = ""

    def __init__(self, name, episode, link, status="watching"):
        self.name = name
        self.status = status
        self.add_episode(episode, link)

    def __str__(self):
        return self.name
    
    def add_episode(self, episode_number, episode_link):
        if(episode_number not in self.episodes):
            self.episodes.append((episode_number, episode_link))

    def status_watching(self):
        self.status = "watching"

    def status_end(self):
        self.status = "ended"

    def status_pending(self):
        self.status = "pending"



# Animes that I follow
myAnimeList = ["Beastars 2nd Season","Re:Zero kara Hajimeru Isekai Seikatsu 2nd Season Part 2","Dr. Stone: Stone Wars",
                "Kumo Desu ga, Nani Ka?","Jujutsu Kaisen (TV)","Shingeki no Kyojin: The Final Season","Log Horizon: Entaku Houkai",
                "Tensei shitara Slime Datta Ken 2nd Season","Yakusoku no Neverland 2nd Season",
                "Tatoeba Last Dungeon Mae no Mura no Shounen ga Joban no Machi de Kurasu Youna Monogatari",
                "Kimetsu no Yaiba Movie: Mugen Ressha-hen","Boku no Hero Academia 5th Season", "One Piece"]

# Url request and get data
url = 'http://jkanime.net'
visitor = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201"}
request = url_request.Request(url,None,visitor)
websiteHTML = url_request.urlopen(request).read()
soup = bs(websiteHTML, 'html.parser')
headers = soup.find_all('a', {'class':"bloqq"})
new_episodes_list = []

print('Latest episodes uploaded:', end='\n\n')
for new_episode in headers:
    anime_name = new_episode.find('div', {'class':"anime__sidebar__comment__item__text"}).find('h5').text
    episode_number = new_episode['href'].split('/')[4]
    episode_link = new_episode['href']
    print("{:50} - {:3} {:50}".format(anime_name,episode_number,episode_link))
    new_episodes_list.append(Anime(anime_name,episode_number,episode_link))

#print("\n{}".format(new_episodes_list), end="\n\n")

#print(headers[0])
#print("*------------------*")
#print(type(headers[0]))
#print(headers[0].find('div', {'class':"anime__sidebar__comment__item__text"}).find('h5').text)


for anime in new_episodes_list:
    print(anime)
newer = [anime.name for anime in new_episodes_list if anime.name in myAnimeList]
print("\n{}".format(newer))

if len(newer) >= 1:
    bt.balloon_tip("Anime Available - Download Now!", "Click on this notification to start download {0}".format(newer[0]))
