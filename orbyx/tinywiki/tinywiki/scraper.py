import logging
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from queue import Queue
from tinywiki.utils import *
from tinywiki.logger import *
from tinywiki.config import *

visited_urls = set()
pages_scraped = 0
urls_to_scrape = Queue()

def scrape_wikipedia(start_url, result, max_pages):
    urls_to_scrape.put(start_url)

    while pages_scraped < int(max_pages):
        current_url = urls_to_scrape.get()
        if current_url in visited_urls:
            continue
        visited_urls.add(current_url)
        if current_url not in result.keys():
            result.setdefault(current_url, {})
        scrape_page(current_url, result)

    logging.info(f"END: Total pages scraped: {pages_scraped}")
    return remove_dangling_children(result)

def scrape_page(url, result):
    global pages_scraped
    content = fetch_page_content(url)
    if content is None:
        logging.info(f"Skipping {url}, content could not be fetched.")
        return 

    soup = BeautifulSoup(content, 'html.parser')

    result[url]["name"] = soup.find(id="firstHeading").get_text()
    result[url]["paragraphs"] = [paragraph.get_text() for paragraph in soup.find_all('p', limit=PARAGRAPH_LIMIT)]
    result[url]["children"] = []
    
    scrape_links_from_content(soup, result[url])
    pages_scraped += 1
    logging.info(f"Number of pages scraped: {pages_scraped}")

def scrape_links_from_content(soup, result):
    for paragraph in soup.find_all('p', limit=PARAGRAPH_LIMIT):
        for link in paragraph.find_all('a', href=True):
            href = link['href']
            if is_wiki_article_url(href):
                result["children"].append(urljoin(BASE_URL, href))
                queue_url_for_scraping(urljoin(BASE_URL, href))
    return result

def queue_url_for_scraping(url):
    if url not in visited_urls:
        urls_to_scrape.put(url)

def remove_dangling_children(result_dictionary):
    for url, info in result_dictionary.items():
        info["children"] = [child for child in info["children"] if child in result_dictionary]
    return result_dictionary

def get_scraped_dictionary(start_url, max_nodes):
    global urls_to_scrape
    scraper_result = {}
    refresh_parameters()
    setup_logging()
    return scrape_wikipedia(start_url, scraper_result, max_nodes)

def refresh_parameters():
    global  urls_to_scrape, visited_urls, pages_scraped
    visited_urls = set()
    pages_scraped = 0
    urls_to_scrape = Queue()
