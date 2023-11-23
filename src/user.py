
from database import Database

class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def set_username(self, username):
        self.username = username

if __name__ == "__main__":
    db = Database()
    usu = User('juano', '123')
    db.login(usu)


