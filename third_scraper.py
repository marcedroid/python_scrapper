from bs4 import BeautifulSoup
import requests

GOOGLE_NEWS_URL = "https://news.google.com/news/?ned=us&hl=en"


def scraping_site():
    re = requests.get(GOOGLE_NEWS_URL)
    if re.status_code == 200:
        soup = BeautifulSoup(re.text, 'html.parser')

        if soup is not None:
            articles = soup.find_all('a', {'class': 'nuEeue'})

            for article in articles:
                print(article.getText())


if __name__ == "__main__":
    scraping_site()