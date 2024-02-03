import logging
import requests
from tinywiki.config import BASE_URL

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

