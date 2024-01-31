import logging
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from queue import Queue
from utils import *
from logger import *
from config import *

visited_urls = set()
pages_scraped = 0

def scrape_page(url):
    global pages_scraped
    content = fetch_page_content(url)
    if content is None: return 
    soup = BeautifulSoup(content, 'html.parser')
    scrape_links_from_content(soup)
    pages_scraped += 1

def scrape_links_from_content(soup):
    for paragraph in soup.find_all('p', limit=3):
        for link in paragraph.find_all('a', href=True):
            href = link['href']
            if is_wiki_article_url(href):
                queue_url_for_scraping(urljoin(BASE_URL, href))

def queue_url_for_scraping(url):
    if url not in visited_urls:
        urls_to_scrape.put(url)

def scrape_wikipedia(start_url):
    urls_to_scrape.put(start_url)

    while not urls_to_scrape.empty() and pages_scraped < MAX_PAGES:
        current_url = urls_to_scrape.get()
        if current_url in visited_urls: continue
        visited_urls.add(current_url)
        scrape_page(current_url)

    logging.info(f"Total pages scraped: {pages_scraped}")

if __name__ == "__main__":
    urls_to_scrape = Queue()
    setup_logging()
    scrape_wikipedia("https://en.wikipedia.org/wiki/Rust_(programming_language)")
    for url in visited_urls:
        print(url)
