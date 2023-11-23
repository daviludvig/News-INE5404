
from tkinter import *
from graphs import Graphs

BACKGROUND_COLOR = "#B3B6B7"
FONT_COLOR = "#1B2631"

class Login_screen(Graphs):
    def __init__(self, root, user):
        super().__init__(root, user)
        self.set_confs()
        self.place_logo()
        self.root.title('Login - INE5404')
        self.place_login_buttons()

    def place_login_buttons(self):
        self.button_login()
        self.button_register()
        self.entry_username()
        self.entry_password()

    def button_login(self):
        button = Button(self.root, text='Login', command=self.login, width=10, height = 3)
        button.configure(background=BACKGROUND_COLOR, fg=FONT_COLOR, font=("Times", 26))
        button.place(x=700, y=100)

    def button_register(self):
        button = Button(self.root, text='Registrar', command=self.register, width=10, height = 3)
        button.configure(background=BACKGROUND_COLOR, fg=FONT_COLOR, font=("Times", 26))
        button.place(x=700, y=300)

    def entry_username(self):
        label = Label(self.root, text='Usuário', font=("Times", 20), bg=BACKGROUND_COLOR, fg=FONT_COLOR)
        label.place(x=30, y=70)

    def entry_password(self):
        label = Label(self.root, text='Senha', font=("Times", 20), bg=BACKGROUND_COLOR, fg=FONT_COLOR)
        label.place(x=30, y=170)

    def login(self):
        self.finish()
        pass

    def register(self):
        self.finish()
        pass



    def finish(self):
        self.root.quit()
