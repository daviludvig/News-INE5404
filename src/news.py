from decouple import config, Csv
from datetime import datetime, timedelta
import os
import requests

class News():
    def __init__(self):
       self.load_api_key()

    def load_api_key(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.api_key = config('NEWS_API_KEY')

    def get_news(self, category, from_date, to_date, country='br'):

        def filter_news_date(news, from_date, to_date):
            filtered_news = []
            for article in news:
                print(article['publishedAt'][:10])
                if from_date <= article['publishedAt'][:10] <= to_date:
                    filtered_news.append(article)
            return filtered_news

        url = f'https://newsapi.org/v2/top-headlines'
        params = {
                'country': country, 
                'category': category, 
                'apiKey': self.api_key,
                  }

        response = requests.get(url, params=params) 

        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'ok':
                return filter_news_date(data['articles'], from_date, to_date)
            else:
                print('Erro ao obter notícias.')
        else:
            print('Erro ao obter notícias.')
            return None
    
    def get_idx_news(self, category, from_date, to_date, idx, country='br'):
        news = self.get_news(category, from_date, to_date, country)
        if news != None:
            if idx < len(news):
                return news[idx]
            else:
                return {'title': 'Não há mais notícias', 'url': '', 'author': '', 'publishedAt': '', 'description': ''}
        else:
            return None

