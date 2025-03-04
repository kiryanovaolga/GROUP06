import sqlite3

path = r'C:\AKADEMIE\GROUP06\projekty\test_projekt\db.sqlite3'

connection = sqlite3.connect(path)
cursor = connection.cursor()

query = 'SELECT * FROM todo_task order by id limit 10'
cursor.execute(query)
data = cursor.fetchall()
print(data)

cursor.execute(f"DELETE FROM todo_task where id < 15")
connection.commit()

if False:
    for n in range(100):
        cursor.execute(f"""
                    INSERT INTO todo_task
                    (title, desc, is_finished, create_dt, update_dt, user_id) values
                    ('Title {n}', 'Description {n}', 0, '2025-01-01', '2025-01-01', 1)
                    """)
        connection.commit()

connection.close()
