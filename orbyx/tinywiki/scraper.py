import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import logging
from queue import Queue

# Configure logging to display information
logging.basicConfig(level=logging.INFO)

# Constants for Wikipedia scraping limits
MAX_DEPTH = 5
MAX_PAGES = 200
BASE_URL = "https://en.wikipedia.org"

# Initialize global variables
visited_urls = set()
pages_scraped = 0

def is_wiki_article_url(url):
    return url.startswith('/wiki/') and not url.startswith('/wiki/Special:')

def fetch_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        logging.error(f"Error fetching {url}: {e}")
        return None

def scrape_page(url, depth):
    global pages_scraped
    content = fetch_page_content(url)
    if content is None: return 

    soup = BeautifulSoup(content, 'html.parser')
    scrape_links_from_content(soup, depth)

    pages_scraped += 1

def scrape_links_from_content(soup, depth):
    for paragraph in soup.find_all('p', limit=3):
        for link in paragraph.find_all('a', href=True):
            href = link['href']
            if is_wiki_article_url(href):
                full_url = urljoin(BASE_URL, href)
                queue_url_for_scraping(full_url, depth)

def queue_url_for_scraping(url, depth):
    if url not in visited_urls and depth < MAX_DEPTH:
        urls_to_scrape.put((url, depth + 1))

def scrape_wikipedia(start_url):
    urls_to_scrape.put((start_url, 1))

    while not urls_to_scrape.empty() and pages_scraped < MAX_PAGES:
        current_url, current_depth = urls_to_scrape.get()
        if current_url in visited_urls: continue

        visited_urls.add(current_url)
        scrape_page(current_url, current_depth)

    logging.info(f"Total pages scraped: {pages_scraped}")

if __name__ == "__main__":
    urls_to_scrape = Queue()
    scrape_wikipedia("https://en.wikipedia.org/wiki/Rust_(programming_language)")
    for url in visited_urls:
        print(url)

