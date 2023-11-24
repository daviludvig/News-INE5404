
# Importing modules
from tkinter import *
from interface import Interface
from login_screen import Login_screen
from user import User

class App():
    def __init__(self, root, user):
        self.login = Login_screen(root, user)
        self.interface = Interface(root, user)

        self.show_login()


    def show_login(self):
        self.login.show(self.show_interface)

    def show_interface(self):
        self.interface.show(self.show_login)

if __name__ == "__main__":
    usu = User()
    root = Tk()
    app = App(root, usu)
