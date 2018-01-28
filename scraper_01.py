import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

url = "http://4ad.com/releases"
uClient = uReq(url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("li", {"class":"color-shape"})

file_name = "album_4ad.csv"
f = open(file_name, "w")
headers = "album_name, artist, release_date, link, image\n"
f.write(headers)

for container in containers:
    try:
        album_info = container.span.text.split("\n")
    except:
        album_container = container.findAll("a")
        album_info = album_container[0].text.split("\n")
    title = album_info[3]
    # title_split = list(title)
    name = title.split("by ")[0]
    artist = title.split("by ")[1]
    release_date = album_info[5].strip()
    link = container.p.a['href']
    image = container.img.get("src")
    f.write(name + "," + artist.replace(",", "&") + "," + release_date + "," + link + "," + image + "\n")

f.close()
