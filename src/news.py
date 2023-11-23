
import requests

class News():
    def __init__(self):
        self.api_key = '06b15464866744d299c3ddda122bb35d'
        self.country = 'br'

    def get_news(self, category):
        url = f'https://newsapi.org/v2/top-headlines'
        params = {'country': self.country, 'category': category, 'apiKey': self.api_key}

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

# if __name__ == "__main__":
#     news = News()
#     if news.get_news('technology') != None:
#         for idx, article in enumerate(news.get_news('technology')):
#             print(f'{idx+1}º notícia:')
#             print(f'Título: {article["title"]}')
#             print(f'Link: {article["url"]}')
#             print(f'Autor: {article["author"]}')
#             print(f'Data de publicação: {article["publishedAt"]}')
#             print(f'Descrição: {article["description"]}')
#             print()
