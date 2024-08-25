# views.py
from django.shortcuts import render, redirect
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'todolist.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        if description:
            Task.objects.create(description=description)
    return redirect('index')

def toggle_tas(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('index')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')
