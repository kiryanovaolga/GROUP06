# tasks.py
import datetime as dt


class Task:
    counter = 0 # class variable
    symbol = '✓'

    def __init__(self, name: str, priority: int = 1, due_dt: dt.datetime = None):
        self.__class__.counter += 1

        self.id = self.counter
        self.name = name
        self.priority = priority
        self.status = False
        self.create_dt = dt.datetime.now()
        self.due_dt = due_dt
    
    def __str__(self):
        symbol = self.symbol if self.status else ' '
        due_dt = f'({self.due_dt})' if self.due_dt else ''
        return f'{self.id}. [{symbol}] {self.name} {due_dt}'

    def finish(self):
        self.status = True

    def undo(self):
        self.status = False


class SuperTask(Task):
    symbol = '✨'


class TaskList:
    def __init__(self, name: str):
        self.name = name
        self.tasks = {}
    
    def add_task(self, task: Task):
        if task.id not in self.tasks:
            self.tasks[task.id] = task

    def remove_task(self, task: Task):
        return self.remove_task_by_id(task.id)

    def remove_task_by_id(self, task_id: int):
        try:
            removed_task = self.tasks.pop(task_id)
            return removed_task
        except KeyError:
            return None
    
    def finish_task_by_id(self, task_id: int):
        """
        dokončete tuto metodu
        1. pomocí task_id získáme instanci Task
        - ze self.tasks
        2. zavoláme na něm metodu finish()
        """
        task: Task = self.tasks[task_id]
        task.finish()
    
    def undo_task_by_id(self, task_id):
        pass
    
    def show(self):
        for task in self.tasks.values():
            print(task)

"""
task_list = TaskList('Pracovní úkoly')
task_list.add_task(Task('Dát si káfe'))
task_list.add_task(Task('Napsat testy'))
task_list.add_task(Task('Zkontrolovat SQL příkazy'))

task_list.finish_task_by_id(3)
task_list.finish_task_by_id(2)

task_list.show()

task_list.undo_task_by_id(2)

task_list.show()
"""