import requests
from bs4 import BeautifulSoup


class NewsParser:
    def __init__(self, url):
        self.url = url
        self.soup = self._get_soup()

    def _get_soup(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return BeautifulSoup(response.text, 'html.parser')
        else:
            raise Exception(f"Ошибка загрузки страницы. Статус: {response.status_code}")

    def parse_news(self):
        news_items = self.soup.find_all('div', class_='list-item')
        news_data = []

        for item in news_items:
            title_tag = item.find('a', class_='list-item__title')
            if title_tag:
                title = title_tag.get_text(strip=True)
                link = title_tag['href']

                news_data.append({
                    'title': title,
                    'link': link
                })

        return news_data