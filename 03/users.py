# users.py

import os, json

DATA_PATH = '03/users.json'

def read_data():
    with open(DATA_PATH, encoding='utf-8') as file:
        return json.load(file)

def write_data(data):
    with open(DATA_PATH, mode="w", encoding='utf-8') as file:
        json.dump(data, file) # zapís do json

def check_password(password, password_repeat):
    if password != password_repeat:
        raise ValueError('Hesla se neshodují')

def check_username(data, username):
    if username in data:
        raise ValueError('Uživatel již existuje')

def register(username, password, password_repeat):
    check_password(password, password_repeat)
    data = read_data()
    check_username(data, username)
    data[username] = password
    write_data(data)

def login(username, password):
    pass

def logout(username):
    pass

def change_password(old_password, password, password_repeat):
    pass

register('test123', 'heslo', 'heslo')