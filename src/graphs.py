
from tkinter import *

BACKGROUND_COLOR = "#B3B6B7"
FONT_COLOR = "#1B2631"

class Graphs():
    def __init__(self, root):
        self.root = root
    
    def set_confs(self):
        self.root.title("Graphs")
        self.root.geometry("1000x500")
        self.root.config(bg=BACKGROUND_COLOR)

    def place_logo(self):
        text = Label(self.root, text="Notícias INE5404", font=("Times", 30), bg=BACKGROUND_COLOR, fg=FONT_COLOR)
        text.pack(side=TOP, pady=20, padx=20, anchor=NW)
