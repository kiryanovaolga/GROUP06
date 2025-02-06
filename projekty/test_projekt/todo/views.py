from django.shortcuts import render
from todo.models import Task


def index(request):
    return render(request, 'todo/index.html')

def todo_list(request):
    tasks = Task.objects.all()[0:100]
    return render(request, 'todo/list.html', {'tasks': tasks})

def todo_new(request):
    return render(request, 'todo/new.html')

def todo_detail(request, number):
    return render(request, 'todo/detail.html')