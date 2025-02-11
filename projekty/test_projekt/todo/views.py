from django import forms
from django.forms import ModelForm
from django.shortcuts import render, redirect
from todo.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'desc'] # atributy z Task
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input'}),
            'desc': forms.Textarea(attrs={'class': 'textarea'}),
        }



def index(request):
    return render(request, 'todo/index.html')

def todo_list(request):
    tasks = Task.objects.all().order_by('-id')[0:100]
    return render(request, 'todo/list.html', {'tasks': tasks})

def todo_new(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save()
            print(task, task.id)
            return redirect('/todo/list/') # todo: opravit
        else:
            form = TaskForm(request.POST)
            return render(request, 'todo/new.html', {'form': form})
    else:
        form = TaskForm()
        return render(request, 'todo/new.html', {'form': form})
    
    

def todo_detail(request, number):
    task = Task.objects.get(id=number)
    return render(request, 'todo/detail.html', {'task': task})