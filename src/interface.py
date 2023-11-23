
# Importing modules
from tkinter import *
from graphs import Graphs
from news import News
from filter import Filter

# Constants
BACKGROUND_COLOR = "#B3B6B7"
FONT_COLOR = "#1B2631"

class Interface(Graphs):
    def __init__(self, root, user):
        super().__init__(root)
        self.user = user
        self.news = News()
        self.idx = -1

        self.set_confs()
        self.root.title('Notícias - INE5404')
        self.place_logo()
        self.place_buttons()

    def place_buttons(self):
        self.button_filter()
        self.button_next_news()
        self.button_past_news()
        self.frame_news()

    def button_filter(self):
        button = Button(self.root, text='Filtro', command=self.filter, width=10, height = 3)
        button.configure(background=BACKGROUND_COLOR, fg=FONT_COLOR, font=("Times", 26))
        button.place(x=700, y=100)
    
    def button_next_news(self):
        button = Button(self.root, text='>', command=self.next_news, width=2, height = 1)
        button.configure(background=BACKGROUND_COLOR, fg=FONT_COLOR, font=("Times", 26))
        button.place(x=830, y=400)

    def button_past_news(self):
        button = Button(self.root, text='<', command=self.past_news, width=2, height = 1)
        button.configure(background=BACKGROUND_COLOR, fg=FONT_COLOR, font=("Times", 26))
        button.place(x=700, y=400)
    
    def frame_news(self):
        frame = Frame(self.root, width=600, height=350)
        frame.configure(background="white")
        frame.place(x=50, y=100)

    def show_news(self, category, country):
        news = self.news.get_idx_news(category, self.idx, country)
        print(news)  
    
    def next_news(self):
        self.idx += 1
        self.show_news(self.filter_window.info['category'], self.filter_window.info['country'])
        pass

    def past_news(self):
        if self.idx > 0:
            self.idx -= 1
        self.show_news(self.filter_window.info['category'], self.filter_window.info['country'])

    def filter(self):
        self.filter_window = Filter(self.root, self.user, self.next_news)
        self.idx = -1

if __name__ == '__main__':
    root = Tk()
    Interface(root, 'user')
    root.mainloop()
