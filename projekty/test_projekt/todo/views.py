from django.shortcuts import render

def index(request):
    return render(request, 'todo/index.html')

def todo_list(request):
    return render(request, 'todo/list.html')

def todo_new(request):
    return render(request, 'todo/new.html')

def todo_detail(request, number):
    return render(request, 'todo/detail.html')