from django.urls import path
from todo import views

app_name = 'todo'

urlpatterns = [
    # /todo/
    path('', views.index, name='index'),
    # /todo/list/
    path('list/', views.todo_list, name='list'),
    # /todo/new/
    path('new/', views.todo_new, name='new'),
    # /todo/7627/
    path('<int:number>/', views.todo_detail, name='detail'),
]