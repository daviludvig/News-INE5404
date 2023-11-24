
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
        super().__init__(root, user)
        self.news = News()
        self.idx = -1

        # self.set_confs()
        # self.root.title('Notícias - INE5404')
        # self.place_logo()
        # self.place_buttons()

    def show(self, show_login):
        self.set_confs()
        self.root.title('Notícias - INE5404')
        self.place_logo()
        self.place_buttons(show_login)
        self.root.mainloop()

    def place_buttons(self, show_login):
        self.button_filter()
        self.button_next_news()
        self.button_past_news()
        self.frame_news()
        self.button_log_out(show_login)

    def button_log_out(self, show_login):
        button = Button(self.root, text='Log out', command= lambda: self.quit(show_login))
        button.configure(background=BACKGROUND_COLOR, fg=FONT_COLOR, font=("Times", 26))
        button.place(x=760, y=20)

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
        backgroud_frame = Frame(self.root, width=600, height=350)
        backgroud_frame.configure(background="white")
        backgroud_frame.place(x=50, y=100)

        self.frame = Frame(self.root, width=600, height=350)
        self.frame.configure(background="white")
        self.frame.place(x=50, y=100)

    def show_news(self, category, country, from_date, to_date):
        
        def open_link(url):
            import webbrowser
            webbrowser.open_new(url)

        for widget in self.frame.winfo_children():
            widget.destroy()
    
        news = self.news.get_idx_news(category, from_date, to_date, self.idx, country)

        if news != None:
            news = {'title': news['title'], 'url': news['url'], 'author': news['author'], 'publishedAt': news['publishedAt'], 'description': news['description']}
        else:
            news = {'title': 'Sem notícias', 'url': '', 'author': '', 'publishedAt': '', 'description': ''}

        title = Label(self.frame, text=news['title'], font=("Times", 20, 'bold'), bg="white", fg=FONT_COLOR, wraplength=570)
        title.pack(side=TOP, padx=5, anchor=NW)
        # title.place(x=0, y=0)
        url = Label(self.frame, text=news['url'], font=("Times", 14), bg="white", fg='blue', wraplength=570, cursor='hand2')
        url.pack(side=BOTTOM, padx=5)
        url.bind("<Button-1>", lambda e: open_link(news['url']))
        author = Label(self.frame, text=news['author'], font=("Times", 14), bg="white", fg=FONT_COLOR)
        # author.place(x=0, y=60)
        author.pack(side=BOTTOM, padx=5, anchor=W)
        publishedAt = Label(self.frame, text=news['publishedAt'], font=("Times", 14), bg="white", fg=FONT_COLOR)
        # publishedAt.place(x=0, y=90)
        publishedAt.pack(side=BOTTOM, padx=5, anchor=W)
        description = Label(self.frame, text=news['description'], font=("Times", 14), bg="white", fg=FONT_COLOR, wraplength=570)
        # description.place(x=0, y=120)
        description.pack(side=BOTTOM, padx=5, anchor=W)

        print(news)  
    
    def next_news(self):
        self.idx += 1
        self.show_news(self.filter_window.info['category'], self.filter_window.info['country'], self.filter_window.info['date_from'], self.filter_window.info['date_to'])

    def past_news(self):
        if self.idx > 0:
            self.idx -= 1
        self.show_news(self.filter_window.info['category'], self.filter_window.info['country'], self.filter_window.info['date_from'], self.filter_window.info['date_to'])


    def filter(self):
        self.filter_window = Filter(self.root, self.user, self.next_news)

        self.idx = -1
    
    def quit(self, show_login):
        for widget in self.root.winfo_children():
            widget.destroy()
        show_login()

