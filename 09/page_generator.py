# page_generator.py

import json

a_element = """
<a href="{url}">
    <img src="{img}" alt="{title}">
    <h2>{title}</h2>
</a>
"""


def gen_list():
    with open('08/data.json', encoding='utf-8') as file:
        data = json.load(file)
        
        result = ''

        for item in data:
            link = a_element.format(
                url = item['url'],
                title = item['title'],
                img = item['img'],
            )

            result += link
        
        return result


def save_list():
    list_html = gen_list()
    # print(list_html)

    with open('09/list.html', encoding='utf-8') as file:
        html = file.read()
        html = html.replace('<!-- HTML -->', list_html)
    
    with open('09/list2.html', mode='w', encoding='utf-8') as file:
        file.write(html)


save_list()
