import urllib.request
import re


def get_title():
    html_file = urllib.request.urlopen("http://econpy.pythonanywhere.com/ex/001.html")
    html_file = html_file.read().decode('utf-8')

    regex = '<div title="buyer-name">(.+?)</div>'

    titles = re.findall(regex, html_file)
    for title in titles:
        print(title)


if __name__ == "__main__":
    get_title()