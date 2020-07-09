# models.py

from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, _id, email, username, password):
        self.id = _id
        self.email = email
        self.username = username
        self.password = password
