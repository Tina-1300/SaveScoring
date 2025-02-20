from bs4 import BeautifulSoup
import requests
import sys 
import time
import re

# https://docs.python.org/fr/3.13/library/time.html

class BaseCrawler():
    
    def __init__(self, stdin = sys.stdin.reconfigure(encoding='utf-8'), stdout = sys.stdout.reconfigure(encoding='utf-8')):
        self.stdin = stdin
        self.stdout = stdout

    # make a loading animation and transform this function into an asynck function
    def request_get_content_source_code_page(self, url:str):
        page_scrore = requests.get(url) 
        while page_scrore.status_code >= 500:
            time.sleep(3)
            page_scrore = requests.get(url)
            if page_scrore.status_code <= 399:
                break
        return page_scrore.text

    def read_content(self, content:str) -> str:
        data = content.encode("utf-8")
        return data 

# no errors
class CrawlerNewbieContest(BaseCrawler):

    def __init__(self):
        BaseCrawler.__init__(self)
    
    # lets find the score for the newbiecontest website
    def find_score(self, content_website:str) -> str:
        soup = BeautifulSoup(self.read_content(content_website), 'html.parser')
        search = soup.find_all('p', {"class" : "bold nospace"})[0].text
        m = re.search(r'\d+', search)
        score = m.group()
        return score
    
    def find_place(self, content_website:str) -> str:
        soup = BeautifulSoup(self.read_content(content_website), 'html.parser')
        search = soup.find_all('span', {"class" : "bold"})[1].text
        m = re.search(r'\d+', search)
        place = m.group()
        return place
    
# no errors
class CrawlerRootMe(BaseCrawler):
    def __init__(self):
        BaseCrawler.__init__(self)

    # lets find the score for the root me website
    def find_score(self, content_website:str) -> str:
        soup = BeautifulSoup(self.read_content(content_website), 'html.parser')
        search = soup.find_all('div', {"class" : "small-6 medium-3 columns text-center"})[1]
        score = search.find("h3").text
        return score

    def find_place(self, content_website:str) -> str:
        soup = BeautifulSoup(self.read_content(content_website), 'html.parser')
        search = soup.find_all('div', {"class" : "small-6 medium-3 columns text-center"})[0]
        place = search.find("h3").text
        return place