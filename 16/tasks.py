# tasks.py
import datetime as dt

class Task:
    counter = 0 # class variable

    def __init__(self, name: str, priority: int = 1, due_dt: dt.datetime = None):
        self.__class__.counter += 1

        self.id = self.counter
        self.name = name
        self.priority = priority
        self.status = False
        self.create_dt = dt.datetime.now()
        self.due_dt = due_dt
    
    def __str__(self):
        symbol = '✓' if self.status else ' '
        due_dt = f'({self.due_dt})' if self.due_dt else ''
        return f'{self.id}. [{symbol}] {self.name} {due_dt}'


task1 = Task('Ukol 1')
task2 = Task("Ukoly 2")
task3 = Task("Ukoly 3", priority=10, due_dt=dt.datetime(2025, 1, 31))
task3.status = True

print(task1)
print(task2)
print(task3)

