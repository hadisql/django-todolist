from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import NewTaskForm, EditTaskForm
from .models import Task, Tag

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
        #selected_tags = Tag.objects.get(pk=request.POST["tags"]) ###
        selected_tags = Tag.objects.filter(pk__in=request.POST.getlist('tags'))

        print(f"NEW TASK, TAGS SELECTED ---------> {selected_tags}")

        if form.is_valid():
            task = form.save(commit=False) #prevents conflict because "created_by" is still not set
            task.created_by = request.user
            task.save()
            task.tags.set(selected_tags) ###

            return redirect('tasks:index')
    else:
        form = NewTaskForm()
        existing_tags = Tag.objects.all()
        print(f"EXISTING TAGS ------> {existing_tags}")

    return render(request, 'tasks/form.html', {
        'form': form,
        'title': 'New Task',
        'existing_tags': existing_tags
    })

@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, created_by=request.user)
    existing_tags = Tag.objects.all()
    print("TASK PRIMARY KEY -------->",task.pk)
    if request.method == "POST":
        form = EditTaskForm(request.POST, instance=task)
        #new_selected_tags = Tag.objects.get(pk=request.POST["tags"]) ###
        new_selected_tags = Tag.objects.filter(pk__in=request.POST.getlist('tags'))

        print(f"EDIT TASK, NEW SELECTED TAGS ---------> {new_selected_tags}")

        if form.is_valid():
            form.save() # "created-by" already exist so we can save directly
            task.tags.set(new_selected_tags) ###
            for tag in existing_tags:
                if tag not in new_selected_tags:
                    task.tags.remove(tag)

            return redirect('tasks:index')#, pk=task.id)
    else:
        form = EditTaskForm(instance=task)
        old_selected_tags = task.tags.all()
        print(f"ALREADY SELECTED TAGS -------> : {old_selected_tags}")


    return render(request, 'tasks/form.html', {
        'form': form,
        'title': 'Edit Task',
        'task': task,
        'old_selected_tags': old_selected_tags,
        'existing_tags': existing_tags
    })

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, created_by=request.user)
    task.delete()

    return redirect('tasks:index')
