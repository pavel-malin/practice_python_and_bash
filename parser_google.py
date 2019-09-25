import urllib.request

from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)

        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if ".ru" in url:
                f = open('url.txt', 'a+')
                f.write(url + '\n')
            if ".com" in url:
                b = open('url.txt', 'a+')
                b.write(url + "\n")

site = "https://news.google.com/?hl=ru&gl=RU&ceid=RU:ru"

Scraper(site).scrape()