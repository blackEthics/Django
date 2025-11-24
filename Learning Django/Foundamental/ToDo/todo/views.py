from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Task

# Create your views here.
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def Mark_As_Done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def Edit_Task(request, pk):
    edited_task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        new_task = request.POST['task']
        edited_task.task = new_task
        edited_task.save()
        return redirect('home')
    else:
        context ={
            'edited_task' : edited_task
        }
        return render(request, 'edit_task.html', context)
    
def Delete_Task(request, pk):
    deleted_task = get_object_or_404(Task, pk=pk)
    deleted_task.delete()
    return redirect('home')

def Undo_Task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')