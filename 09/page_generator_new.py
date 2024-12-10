"""
page_generator_new.py
nová upravená verze - každá fukce dělá jednu věc
"""

import json


def read_json_data():
    with open('08/data.json', encoding='utf-8') as file:
        return json.load(file)

def read_template():
    with open('09/list.html', encoding='utf-8') as file:
        return file.read()

def save_html(html):
    with open('09/list3.html', mode='w', encoding='utf-8') as file:
        file.write(html)

def get_list_html(data):
    indentation = '\n' + ' ' * 12 # nový rádek + 12 mezer
    item_template = '<a href="{url}"><img src="{img}" alt="{title}"><h2>{title}</h2></a>'
    return indentation.join(item_template.format(**item) for item in data)

def main():
    template = read_template()
    data = read_json_data()
    html = get_list_html(data)
    html = template.replace('<!-- HTML -->', html)
    save_html(html)


main()
