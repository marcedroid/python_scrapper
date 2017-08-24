import json
import re
import threading
import requests
from pymongo import MongoClient

USERNAME = 'wwe'
URL = 'https://www.instagram.com/' + USERNAME


def set_threading(node, database):
    get_id = node['id']
    src = node['thumbnail_src']
    caption = node['caption']
    comments = node['comments']['count']
    likes = node['likes']['count']

    json_insert = {'id': get_id, 'src': src, 'caption': caption, 'comments': comments, 'likes': likes}
    database.instagram.insert(json_insert)

    print('save', get_id)


def get_soup(url):
    soup = requests.get(url)
    if soup.status_code == 200:
        return soup.text


def run_bot():
    soup = get_soup(URL)

    client = MongoClient('localhost', 27017)
    database = client.test_scraper

    if soup is not None:
        regex = '<script type="text/javascript">window._sharedData = (.+?);</script>'
        script = re.findall(regex, requests.get(URL).text)[0]
        obj = json.loads(script)
        nodes = obj['entry_data']['ProfilePage'][0]['user']['media']['nodes']

        for node in nodes:
            robot = threading.Thread(name='set_threading', target=set_threading, args=(node, database))
            robot.start()


if __name__ == '__main__':
    run_bot()
