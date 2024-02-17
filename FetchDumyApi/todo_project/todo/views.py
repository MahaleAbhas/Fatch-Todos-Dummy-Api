from django.shortcuts import render
from .models import Todo
import requests

def home_page(request):
    response = requests.get("https://dummyjson.com/todos")
    if response.status_code == 200:
        data = response.json()
        todos = data.get('todos')
        for to in todos:
            obj, created = Todo.objects.get_or_create(**to)
            print(obj, created)
    obj_lis = Todo.objects.all()
    context = {'obj_lis':obj_lis}
    return render(request,'temp/home.html', context=context)


