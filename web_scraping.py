import requests
from bs4 import BeautifulSoup
import logging
from configparser import load_config

class WebScraper:
    def __init__(self):
        self.toppr_url = config['web_scraping']['toppr_url']
        self.byjus_url = config['web_scraping']['byjus_url']
        self.brainly_url = config['web_scraping']['brainly_url']
        self.logger = logging.getLogger(__name__)
    
    def scrape_toppr(self, query):
        self.logger.info(f"Scraping toppr for Query : {query}")
        response = requests.get(f"{self.toppr_url}/search?term={query}")
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            return self.extract_content(soup)
        return None
    
    def scrape_byjus(self, query):
        self.logger.info(f"Scraping byjus for Query : {query}")
        response = requests.get(f"{self.byjus_url}/search?term={query}")
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            return self.extract_content(soup)
        return None
    
    def scrape_brainly(self, query):
        self.logger.info(f"Scraping brainly for Query : {query}")
        response = requests.get(f"{self.brainly_url}/search?term={query}")
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            return self.extract_content(soup)
        return None
    
    def extract_content(self, soup):
        content = soup.find_all('div', class_= 'content')
        return [c.text for c in content]
    
if __name__ == '__main__':
    config = load_config()
    scraper = WebScraper()
    print(scraper.scrape_toppr("Pythagorean Theorem"))