from django import forms
from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
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
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user).order_by('-id')[0:100]
        return render(request, 'todo/list.html', {'tasks': tasks})
    else:
        return redirect('/todo/')

def todo_detail(request, number):
    # ošetřete toto view, aby zobrazovalo pouze task
    # 1) přihlášený uživatel
    # 2) task musí patřit tomuto uživatel
    # 3) v opačném případě redirect na '/todo/'
    if request.user.is_authenticated:
        task = get_object_or_404(Task, id=number)
        # task = Task.objects.get(id=number)
        
        if task.user == request.user:
            return render(request, 'todo/detail.html', {'task': task})
    
    return redirect('/todo/')

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
    
    

