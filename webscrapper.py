import requests
from bs4 import BeautifulSoup as bs


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
        full_url = 'https://www.google.com/search?q=' + topic + '&source=lnms&tbm=nws'+current_page
        # fullUrl = 'https://www.google.com/search?q=gme&source=lnms&tbm=nws' + currentPage
        url = requests.get(full_url)
        soup = bs(url.content, 'html.parser')
        # a tags that hold the href link
        a_tags = soup.find_all('a')
        for content in a_tags:
            # gets link associated with href tag
            link = content.get('href')
            # filters out the non articles
            if 'url?q=' in link:
                # article title
                text = str(content.text)
                if text.lower() is not 'learn more' or text.lower() is not 'sign in':
                    # gets article link, removing the google redirect
                    # link = str(link).split('url?q=')[1]
                    # links.add(link)
                    # adds article link with the title
                    # links[text] = link
                    links.add(text)
    return links
