import datetime as dt
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from todo.models import Task
from todo.forms import TaskForm


def index(request):
    return render(request, 'todo/index.html')


def todo_list(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
        # ?active
        if 'active' in request.GET:
            tasks = tasks.filter(is_finished=False)
        elif 'finished' in request.GET:
            tasks = tasks.filter(is_finished=True)

        tasks = tasks.order_by('-id')[0:100]
        return render(request, 'todo/list.html', {'tasks': tasks, 'dt_now': dt.datetime.now()})
    else:
        return redirect('/todo/')

def todo_detail(request, number):
    # ošetřete toto view, aby zobrazovalo pouze task
    # 1) přihlášený uživatel
    # 2) task musí patřit tomuto uživatel
    # 3) v opačném případě redirect na '/todo/'
    if request.user.is_authenticated:
        task = get_object_or_404(Task, id=number)
        
        if task.user == request.user:
            if request.method == 'POST':
                form = TaskForm(request.POST, instance=task)
                if form.is_valid():
                    form.save()
                    return redirect('/todo/list/')
            else:
                form = TaskForm(instance=task)
            return render(request, 'todo/detail.html', {'task': task, 'form': form})
    
    return redirect('/todo/')

def todo_new(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TaskForm(request.POST)

            if form.is_valid():
                task = form.save(commit=False)
                task.user = request.user
                task.save()

                print(task, task.id)
                return redirect('/todo/list/') # todo: opravit
        else:
            form = TaskForm()

        return render(request, 'todo/new.html', {'form': form})
    else:
        return redirect('/todo/')
 
# /todo/232789/delete/
def todo_task_delete(request, number):
    """
    1. najdeme ho
        a) podle number id=number
        b) user musí přihlašení
        c) task musí patřit uživateli
    2. smažeme ho 
    3. zobrazit list
    """
    if request.method == 'POST':
        if request.user.is_authenticated:
            task = get_object_or_404(Task, id=number, user=request.user)
            task.delete()
            return redirect('/todo/list/')

    return redirect('/todo/')


def todo_task_finish(request, number):
    if request.method == 'POST':
        if request.user.is_authenticated:
            task = get_object_or_404(Task, id=number, user=request.user)

            task.is_finished = not task.is_finished

            """
            if task.is_finished:
                task.is_finished = False
            else:
                task.is_finished = True
            """
            
            task.save(update_fields=['is_finished'])
            return redirect('/todo/list/')

    return redirect('/todo/')

"""
1. definovat url cestu

2. definovat view
získame si task stejně jako u delete
task.is_finished = True
task.save()

3. přidat form do template


"""