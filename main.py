import requests
from bs4 import BeautifulSoup
import json

HOST = 'https://www.avforums.com'
URL = HOST + '/threads/samsung-q80t-qe55q80t-review-comments.2328417/'
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15'
}


def get_html(url, params=None):
    response = requests.get(url, params=params, headers=HEADERS)
    return response


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('article', class_='message')

    parsed_data = list(map(lambda item: {
                'author': item.find('h4', class_='message-name').get_text(strip=True),
                'author_link': HOST + item.find('div', class_='message-userDetails').find('a').get('href'),
                'author_title': item.find('h5', class_='userTitle').get_text(),
                'date': item.find('div', class_='message-attribution-main').get_text(strip=True),
                'content': item.find('div', class_='message-content').get_text(strip=True)
            }, items))

    return parsed_data


def parse():
    html = get_html(URL)
    print(get_content(html.text))
parse()
