
from tkinter import *
from tkinter import messagebox
from graphs import Graphs
import hashlib
import os

BACKGROUND_COLOR = "#B3B6B7"
FONT_COLOR = "#1B2631"

class Login_screen(Graphs):
    def __init__(self, root, user):
        super().__init__(root, user)
        # self.set_confs()
        # self.place_logo()
        # self.root.title('Login - INE5404')
        # self.place_login_buttons()

    def show(self, show_interface):
        self.set_confs()
        self.place_logo()
        self.root.title('Login - INE5404')
        self.place_login_buttons(show_interface)
        self.root.mainloop()

    def place_login_buttons(self, show_interface):
        self.button_login(show_interface)
        self.button_register(show_interface)
        self.set_entry_username()
        self.set_entry_password(show_interface)

    def button_login(self, show_interface):
        button = Button(self.root, text='Login', command= lambda: self.login(show_interface), width=10, height = 3)
        button.configure(background=BACKGROUND_COLOR, fg=FONT_COLOR, font=("Times", 26))
        button.place(x=700, y=100)

    def button_register(self, show_interface):
        button = Button(self.root, text='Registrar', command= lambda: self.place_register_buttons(show_interface), width=10, height = 3)
        button.configure(background=BACKGROUND_COLOR, fg=FONT_COLOR, font=("Times", 26))
        button.place(x=700, y=300)

    def set_entry_username(self, insert=''):
        label = Label(self.root, text='Usuário', font=("Times", 24), bg=BACKGROUND_COLOR, fg=FONT_COLOR)
        label.place(x=100, y=100)

        self.entry_username = Entry(self.root, width=30, font=("Times", 24), bg="white", fg="black")
        self.entry_username.place(x=100, y=140)
        self.entry_username.insert(0, insert)

    def set_entry_password(self, show_interface):
        label = Label(self.root, text='Senha', font=("Times", 24), bg=BACKGROUND_COLOR, fg=FONT_COLOR)
        label.place(x=100, y=210)

        self.entry_password = Entry(self.root, width=30, font=("Times", 24), bg="white", fg="black", show='*')
        self.entry_password.place(x=100, y=250)
        self.entry_password.bind('<Return>', lambda event: self.login(show_interface))

    def login(self, show_interface):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path = dir_path.replace('src', 'docs')
        dir_path = dir_path + f'/accounts/{self.entry_username.get()}.txt'

        if not os.path.exists(dir_path):
            messagebox.showerror("Erro", "Usuário não existe")
            return False
        
        with open (dir_path, 'r') as file:
            info = file.read().split('; ')
            file.close()

        if info[0] != self.entry_username.get() or info[1] != self.hash_password(self.entry_password.get()):
            messagebox.showerror("Erro", "Usuário ou senha incorretos")
            self.entry_password.delete(0, END)
            return False

        self.user.set_username(self.entry_username.get())
        self.user.set_password(self.entry_password.get())

        messagebox.showinfo("Sucesso", "Login realizado com sucesso")
        self.quit(show_interface)

    def register(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path = dir_path.replace('src', 'docs')
        dir_path = dir_path + f'/accounts/{self.entry_username.get()}.txt'
        print(dir_path)

        if os.path.exists(dir_path):
            messagebox.showerror("Erro", "Usuário já existe")
            return False

        with open (dir_path, 'w') as file:
            file.write(f'{self.entry_username.get()}; ')
            file.write(f'{self.hash_password(self.entry_password.get())}')
            file.close()
        return True
        

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
   
    def check_insert_db(self, show_interface):
        def check_info():
            if self.entry_username.get() == '' or self.entry_password.get() == '':
                messagebox.showerror("Erro", "Preencha todos os campos")
                return False
            
            elif self.entry_password.get() == self.entry_password_confirm.get():
                return True

            else:
                messagebox.showerror("Erro", "As senhas não coincidem")
                self.entry_password.delete(0, END)
                self.entry_password_confirm.delete(0, END)
                return False

        var1 = self.entry_username.get()
        var2 = self.hash_password(self.entry_password.get())
    
        if not check_info():
            return

        if self.register():
            messagebox.showinfo("Sucesso", "Usuário registrado com sucesso")
            for widget in self.root.winfo_children():
                widget.destroy()
            self.place_logo()
            self.button_login(show_interface)
            self.button_register(show_interface)
            self.set_entry_username(var1)
            self.set_entry_password(show_interface)
    
        else:
            self.entry_username.delete(0, END)
            self.entry_password.delete(0, END)
            self.entry_password_confirm.delete(0, END)

    def button_confirm_register(self, show_interface):
        button = Button(self.root, text='Confirmar', command= lambda:self.check_insert_db(show_interface), width=10, height = 3)
        button.configure(background=BACKGROUND_COLOR, fg=FONT_COLOR, font=("Times", 26))
        button.place(x=700, y=100)


    def button_cancel_register(self, show_interface):
         
        def cancel():
            for widget in self.root.winfo_children():
                widget.destroy()
            
            self.place_logo()
            self.button_register(show_interface)
            self.button_login(show_interface)
            self.set_entry_username()
            self.set_entry_password(show_interface)

        button = Button(self.root, text='Cancelar', command=cancel, width=10, height = 3)
        button.configure(background=BACKGROUND_COLOR, fg=FONT_COLOR, font=("Times", 26))
        button.place(x=700, y=300)

    def place_register_buttons(self, show_interface):
        for widget in self.root.winfo_children():
            if widget.winfo_class() == 'Button':
                widget.destroy()

        self.button_confirm_register(show_interface)
        self.button_cancel_register(show_interface)

        self.entry_password.delete(0, END)

        label = Label(self.root, text='Confirmar senha', font=("Times", 24), bg=BACKGROUND_COLOR, fg=FONT_COLOR)
        label.place(x=100, y=320)

        self.entry_password_confirm = Entry(self.root, width=30, font=("Times", 24), bg="white", fg="black", show='*')
        self.entry_password_confirm.place(x=100, y=360)

        self.entry_password_confirm.bind('<Return>', lambda event: self.check_insert_db(show_interface))
        self.entry_password.unbind('<Return>')

    def quit(self, show_interface):
        for widget in self.root.winfo_children():
            widget.destroy()
        show_interface()
