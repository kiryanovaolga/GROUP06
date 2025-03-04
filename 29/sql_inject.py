# sql_inject.py

import sqlite3

path = r'C:\AKADEMIE\GROUP06\projekty\test_projekt\db.sqlite3'
connection = sqlite3.connect(path)
cursor = connection.cursor()

search_text = input('Zadej hledání: ')

query = f" SELECT * FROM todo_task where title like '?%' and user_id = ?"

print(query)

exit()

cursor.execute(query, [search_text, 1])

data = cursor.fetchall() # [(1, 'title', 'desc' ...), (2, 'title', 'desc' ...)]

for item in data:
    print(item[0], item[1])


