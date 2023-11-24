
from tkinter import *
from tkinter import messagebox
from datetime import datetime

BACKGROUND_COLOR = "#B3B6B7"
FONT_COLOR = "#1B2631"

COUNTRIES = ["ae", "ar", "at", "au", "be", "bg", "br", "ca", "ch", "cn", "co", "cu", "cz", "de", "eg", "fr", "gb", "gr", "hk", "hu", "id", "ie", "il", "in", "it", "jp", "kr", "lt", "lv", "ma", "mx", "my", "ng", "nl", "no", "nz", "ph", "pl", "pt", "ro", "rs", "ru", "sa", "se", "sg", "si", "sk", "th", "tr", "tw", "ua", "us", "ve", "za"]
CATEGORYS = ["business", "entertainment", "general", "health", "science", "sports", "technology", "politics"]


class Filter(Toplevel):
    def __init__(self, root, user, next_news):
        super().__init__(root)
        self.user = user
        self.set_confs(next_news)
    
    def set_confs(self, next_news):
        self.configure(background=BACKGROUND_COLOR)
        self.geometry('400x500')
        self.resizable(False, False)
        self.title(f'Filtro {self.user.get_username()} - INE5404')
        self.place_logo()
        self.place_buttons(next_news)

    def place_buttons(self, next_news):
        self.button_filter(next_news)
        self.entry_date_from()
        self.entry_date_to()
        self.entry_category()
        self.entry_country()
        if self.user.filter != {}:
            self.date_from.insert(0, self.user.filter['date_from'])
            self.date_to.insert(0, self.user.filter['date_to'])
            self.category.insert(0, self.user.filter['category'])
            self.country.insert(0, self.user.filter['country'])

    def place_logo(self):
        text = Label(self, text='Filtro INE5404', font=("Times", 20), bg=BACKGROUND_COLOR, fg=FONT_COLOR)
        text.pack(side=TOP, pady=20)

    def button_filter(self, next_news):
        button = Button(self, text='Filtrar', command= lambda: self.finish(next_news), width=10)
        button.configure(background=BACKGROUND_COLOR, fg=FONT_COLOR, font=("Times", 26))
        button.pack(side=BOTTOM, pady=60)
    
    def entry_date_from(self):
        self.date_from = Entry(self, width=15, font=("Times", 15))
        label = Label(self, text='Data inicial', font=("Times", 20), bg=BACKGROUND_COLOR, fg=FONT_COLOR)
        label.place(x=30, y=70)
        self.date_from.place(x=30, y=110)

    def entry_date_to(self):

        today = datetime.now()

        today = today.strftime('%Y-%m-%d')

        self.date_to = Entry(self, width=15, font=("Times", 15))
        label = Label(self, text='Data final', font=("Times", 20), bg=BACKGROUND_COLOR, fg=FONT_COLOR)
        label.place(x=220, y=70)
        self.date_to.place(x=220, y=110)
        if self.user.filter == {}:
            self.date_to.insert(0, today)

    def entry_category(self):
        self.category = Entry(self, width=20, font=("Times", 15))
        label = Label(self, text='Assunto', font=("Times", 20), bg=BACKGROUND_COLOR, fg=FONT_COLOR)
        label.place(x=30, y=170)
        self.category.place(x=30, y=210)

    def entry_country(self):
        self.country = Entry(self, width=5, font=("Times", 15))
        label = Label(self, text='País', font=("Times", 20), bg=BACKGROUND_COLOR, fg=FONT_COLOR)
        label.place(x=280, y=170)
        self.country.place(x=280, y=210)

        if self.user.filter == {}:
            self.country.insert(0, 'br')

    def finish(self, next_news):

        def analysis_date(date):
            try:
                datetime.strptime(date, '%Y-%m-%d')
                return True
            except:
                return False

        date_from = self.date_from.get()
        date_to = self.date_to.get()
        category = self.category.get()
        country = self.country.get()
       
        if date_from == '' or date_to == '' or category == '' or country == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

        if len(country) != 2 or country not in COUNTRIES:
            messagebox.showerror('Erro', 'País inválido')
            return

        if len(category) > 30 or category not in CATEGORYS:
            messagebox.showerror('Erro', 'Assunto inválido')
            return

        if len(date_from) != 10 or len(date_to) != 10 or not analysis_date(date_from) or not analysis_date(date_to):
            messagebox.showerror('Erro', 'Data inválida')
            return

        datetime_from = datetime.strptime(date_from, '%Y-%m-%d')
        datetime_to = datetime.strptime(date_to, '%Y-%m-%d')
        today_datetime = datetime.now()#.date()

        if (date_from > date_to) or (datetime_from > today_datetime) or (datetime_to > today_datetime):
            messagebox.showerror('Erro', 'Datas indevidas')
            return
        
        self.info = {'date_from': date_from, 'date_to': date_to, 'category': category, 'country': country}
        self.user.set_filter(self.info)
        # self.quit()

        self.destroy()
        next_news()
