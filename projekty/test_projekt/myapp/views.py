from django.http import HttpResponse
from django.shortcuts import render
import random
import datetime as dt

def index_page(request):
    print(request.method)
    print(request.path)
    
    number = random.randint(1, 100)
    d = dt.datetime.now()

    return HttpResponse(f'''
                        <h1>Hello From Django: {number} | {d}</h1>
                        <img src="https://picsum.photos/200/300">
                        ''')


def url_paths(request):

    print(request.GET)
    print(request.GET['xyz'])
    print(request.GET.getlist('xyz'))
    # ?key=value&xyz=10&xyz=20

    return HttpResponse('This page is working')


def my_math(request):
    """
    /my-math/?operation=plus&a=10&b=100
    operation=plus | minus | multiple | divide
    a=první číslo
    b=druhé číslo
    """
    a = int(request.GET['a'])
    b = int(request.GET['b'])
    operation = request.GET['operation']

    if operation == 'plus':
        result = a + b
    elif operation == 'minus':
        result = a - b

    return HttpResponse(f'RESULT: {result}')


# MVC - model view controller (ovladač)
# MVT - model view (pohled) - template (HTML šablona)


"""
try:
    name = request.GET['name']
except KeyError:
    name = 'World'

if 'name' in request.GET:
    name = request.GET['name']
else:
    name = 'World'
"""

def test_template(request):
    print(request.GET)
    name = request.GET.get('name', 'World')
    age = request.GET.get('age', 0)
    # záskejte klíč age, pokud age není tak doplňte 0

    age = int(age) if age.isdecimal() else 0

    context = {
        'date': dt.datetime.now(),
        'name': name,
        'age': age,
    }
    # render = vykreslit
    return render(request, 'test_template.html', context)

# dodělat select pro operace a post form
def calculator(request):
    try:    
        a = int(request.GET['a'])
        b = int(request.GET['b'])
        result = a + b
    except (KeyError, TypeError, ValueError):
        result = ''

    context = {
        'result': result
    }

    return render(request, 'calculator.html', context)


"""
úkol: vytvořte zde view s názvem time_page
pamatujte: na vstupu musí být request a na výstupu HttpResponse
"""
