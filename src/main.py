
# Importing modules
from tkinter import *
from interface import Interface
from login_screen import Login_screen
from user import User

class App():
    def __init__(self, root, user):
        self.login = Login_screen(root, user)
        root.mainloop()

if __name__ == "__main__":
    usu = User()
    root = Tk()
    app = App(root, usu)
