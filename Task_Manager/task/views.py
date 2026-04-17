from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskFrom

# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def create_task(request):
    if request.method == "POST":
        form = TaskFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form: TaskFrom() # type: ignore
    return render(request, 'tasks/create_task.html', {'form': form})

def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == "POST":
        form = TaskFrom(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskFrom(instance=task)
    return render(request, 'tasks/update_task.html', {'form': form})

def delete_task(request, pk):
    task = Task.objets.get(pk = pk)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')