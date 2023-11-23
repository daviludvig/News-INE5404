
from database import Database

class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.filter = {}

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def set_username(self, username):
        self.username = username

    def set_filter(self, date_from, date_to, category, country='br'):
        self.filter['date_from'] = date_from
        self.filter['date_to'] = date_to
        self.filter['category'] = category
        self.filter['country'] = country

if __name__ == "__main__":
    db = Database()
    usu = User('juano', '123')
    db.login(usu)


