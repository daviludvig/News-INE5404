
from database import Database

class User():
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
        self.filter = {}

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def set_username(self, username):
        self.username = username

    def set_filter(self, in_filter):
        self.filter = in_filter

if __name__ == "__main__":
    db = Database()
    usu = User('juano', '123')
    db.login(usu)


