# svatky_app.py

import json

with open('05/svatky.json', mode='r', encoding='utf-8') as file:
    data = json.load(file)
    # print(data)

print(data['1501'])


def find_day(name):
    for key, value in data.items():
        if name in value:
            return key


print(find_day('Bohdana'))
