from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import NewTaskForm, EditTaskForm
from .models import Task

# Create your views here.


@login_required
def index(request):
    #tasks = get_object_or_404(Task, pk=pk)
    tasks = Task.objects.filter(created_by=request.user)

    return render(request, 'tasks/index.html',{
        'tasks':tasks
    })

@login_required
def new_task(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False) #prevents conflict because "created_by" is still not set
            task.created_by = request.user
            task.save()

            return redirect('tasks:index')#, pk=task.id)
    else:
        form = NewTaskForm()

    return render(request, 'tasks/form.html', {
        'form': form,
        'title': 'New Task'
    })

@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, created_by=request.user)
    print("TASK PRIMARY KEY !!!!!!!!",task.pk)
    if request.method == "POST":
        form = EditTaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save() # "created-by" already exist so we can save directly

            return redirect('tasks:index')#, pk=task.id)
    else:
        form = EditTaskForm(instance=task)

    return render(request, 'tasks/form.html', {
        'form': form,
        'title': 'Edit Task',
        'task': task
    })

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, created_by=request.user)
    task.delete()

    return redirect('tasks:index')
