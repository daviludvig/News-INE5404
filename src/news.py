from decouple import Config, Csv

import requests

class News():
    def __init__(self):
       self.load_api_key()

    def load_api_key(self):
        config = Config()
        config.read_dotenv()
        self.api_key = config('NEWS_API_KEY')

    def get_news(self, category, country='br'):
        url = f'https://newsapi.org/v2/top-headlines'
        params = {
                'country': country, 
                'category': category, 
                'apiKey': self.api_key
                  }

        response = requests.get(url, params=params) 

        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'ok':
                return data['articles']
            else:
                print('Erro ao obter notícias.')
        else:
            print('Erro ao obter notícias.')
            return None
    
    def get_idx_news(self, category, idx, country='br'):
        news = self.get_news(category, country)
        if news != None:
            return news[idx]
        else:
            return None

# if __name__ == "__main__":
#     news = News()
#     if news.get_news('health') != None:
#         for idx, article in enumerate(news.get_news('politics')):
#             print(f'{idx+1}º notícia:')
#             print(f'Título: {article["title"]}')
#             print(f'Link: {article["url"]}')
#             print(f'Autor: {article["author"]}')
#             print(f'Data de publicação: {article["publishedAt"]}')
#             print(f'Descrição: {article["description"]}')
#             print()
