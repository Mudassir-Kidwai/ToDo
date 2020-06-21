from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    forms = TaskForm()

    if request.method == 'POST':
        forms = TaskForm(request.POST)
        if forms.is_valid():
            forms.save()
        return redirect('/')

    context = {'tasks':tasks, 'forms':forms}
    return render(request, 'task/list.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    forms = TaskForm(instance=task)
    if request.method == 'POST':
        forms = TaskForm(request.POST, instance=task)
        if forms.is_valid():
            forms.save()
            return redirect('/')
 
    context = {'forms':forms}
    
    return render(request, 'task/update_task.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    context = {'item':item}
    if request.method == 'POST':
        item.delete()
        return redirect('/')
        
    return render(request, 'task/delete_task.html', context)