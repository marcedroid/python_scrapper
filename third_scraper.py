from bs4 import BeautifulSoup
from pymongo import MongoClient
import requests
import threading


GOOGLE_NEWS_URL = "https://news.google.com/news/?ned=us&hl=en"
MATCH_URL = 'gizmodo.com'


def get_beautiful_soup(url):
    re = requests.get(url)
    if re.status_code == 200:
        return BeautifulSoup(re.text, 'html.parser')


def set_robot(article, database):
    title = article.getText()
    href = article.get('href')

    if MATCH_URL in href:
        soup = get_beautiful_soup(href)

        if soup is not None:
            container = soup.find('div', {'class': 'post-content entry-content js_entry-content '})
            json = {'title': title, 'href': href, 'content': container.getText()}
            database.articles.insert(json)
            print('Save', title)


def scraping_site():
    soup = get_beautiful_soup(GOOGLE_NEWS_URL)
    if soup is not None:
        client = MongoClient('localhost', 27017)
        database = client.test_scraper

        articles = soup.find_all('a', {'class': 'nuEeue'})

        for article in articles:
            robot = threading.Thread(name='set_robot', target=set_robot, args=(article, database))
            robot.start()


if __name__ == "__main__":
    scraping_site()