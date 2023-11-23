
import os
import hashlib


class Database():
    def __init__(self):
        path = os.path.dirname(os.path.abspath(__file__))
        self.path = path[:-4] + '/docs/accounts/'

    def hashing(self, target):
        return hashlib.sha256(target.encode()).hexdigest()

    def register(self, user):
            file_name = user.get_username() + '.txt'

            path = self.path + file_name

            if not os.path.exists(path):
                with open(path, 'w') as file:
                    file.write(user.get_username() + '; ')
                    file.write(self.hashing(user.get_password()))
                    print('Usuário criado com êxito.')
            else:
                print('Usuário já existente.')
                return
    
    def login(self, user):
        file_name = user.get_username() + '.txt'

        path = self.path + file_name

        if os.path.exists(path):
            with open(path, 'r') as file:
                data = file.read()
                data = data.split('; ')
                if data[0] == user.get_username() and data[1] == self.hashing(user.get_password()):
                    print('Login efetuado com êxito.')
                else:
                    print('Senha incorreta.')
        else:
            print('Usuário não existente.')
            return
