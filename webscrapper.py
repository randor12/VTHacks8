import requests
from bs4 import BeautifulSoup as bs
import re


def scraper(topic, num_pages):
    """
    Function scraps numPages pages from google search for news on the topic
    and gets the article titles for those search results


    @:param topic, the keyword to search
    @:param numPages, the number of pages to search
    @:return returns set of article titles
    """
    # links = {}
    links = set()
    # sub for page number
    page_stub = '&start='
    # range is page up to page number
    for page in range(num_pages):
        # calculates page number as stub is based upon 10 results a page
        current_page = page_stub + (str(page * 10))
        # the full url
        full_url = 'https://www.google.com/search?q=' + topic + '&source=lnms&tbm=nws' + current_page
        url = requests.get(full_url)
        soup = bs(url.content, 'html.parser')
        soup.encode("utf-8", errors='replace')
        # a tags that hold the href link
        a_tags = soup.find_all('a')
        for content in a_tags:
            # gets link associated with href tag
            link = content.get('href')
            # filters out the non articles
            if 'url?q=' in link:
                # article title
                # filter out special characters
                text = re.sub("[-.,!_?]", " ", str(content.text))
                # adds article title to set
                links.add(text)
    links.remove('Learn more')
    links.remove('Sign in')
    return links
