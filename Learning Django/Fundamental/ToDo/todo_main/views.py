
from django.shortcuts import render
from django.http import HttpResponse

from todo.models import Task


def home(request):
    tasks = Task.objects.filter(is_completed = False)
    completed_tasks = Task.objects.filter(is_completed = True)
    print(tasks)
    context = {
        'tasks' : tasks,
        'completed_tasks' : completed_tasks
    }
    return render(request, 'home.html', context)