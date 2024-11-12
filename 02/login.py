data = {
    'jakub': 'heslo1',
    'jana': 'heslo2',
    'petr': 'heslo3',
}

username = input('Zadej username: ')
password = input('Zadej heslo: ')

error_text = 'přihlašení se nepodařilo ...'
"""
if username in data and password == data[username]:
    print('OK')
else:
    print(error_text)
"""

try:
    assert data[username] == password
    print('OK')
except:
    print(error_text)
