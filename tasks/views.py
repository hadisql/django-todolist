from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
# from django.db.models import Q
# from functools import reduce

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
        selected_tags = Tag.objects.filter(pk__in=request.POST.getlist('tags')) #tags selected amongst the existing ones

        new_custom_tags = []
        for custom_tag in request.POST['custom_tags'].split():
            new_custom_tags.append(Tag.objects.create(name=custom_tag)) #add each new tag in Tag objects

        print(f"NEW TASK, TAGS SELECTED ---------> {selected_tags}")
        #print(f"TASKS CUSTOM : --------> {Tag.objects.filter(reduce(lambda x,y: x | y, [Q(name__contains=word) for word in new_custom_tags]))}") #https://stackoverflow.com/questions/7088173/how-to-query-model-where-name-contains-any-word-in-python-list
        print(f"CUSTOM TAGS OBJECT LIST: --------> {Tag.objects.filter(name__in=new_custom_tags)}")

        print(f"UNION OBJECT LIST : ------> {selected_tags.union(Tag.objects.filter(name__in=new_custom_tags))}")

        if form.is_valid():
            task = form.save(commit=False) #prevents conflict because "created_by" is still not set
            task.created_by = request.user
            task.save()
            task.tags.set(selected_tags.union(Tag.objects.filter(name__in=new_custom_tags))) # adding the selected tags + new custom tags


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

        new_selected_tags = Tag.objects.filter(pk__in=request.POST.getlist('tags'))

        print(f"EDIT TASK, NEW SELECTED TAGS ---------> {new_selected_tags}")
        new_custom_tags = []
        for custom_tag in request.POST['custom_tags'].split():
            new_custom_tags.append(Tag.objects.create(name=custom_tag))
        print(f"NEW CUSTOM TAG ADDED : --------> {new_custom_tags}")

        if form.is_valid():
            form.save() # "created-by" already exist so we can save directly
            task.tags.set(new_selected_tags.union(Tag.objects.filter(name__in=new_custom_tags))) # adding the selected tags + new custom tags

            for tag in existing_tags: #if tag unselected, we remove it from task
                if tag not in (new_selected_tags.union(Tag.objects.filter(name__in=new_custom_tags))):
                    task.tags.remove(tag)

            return redirect('tasks:index')
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

@login_required
def edit_tags(request):
    tags = Tag.objects.all()

    if request.method == "POST":
        for tag in request.POST:
            print("selected tag ---------->",tag)
            Tag.objects.filter(name=tag).delete()

    return render(request, 'tasks/tags.html', {
        'tags': tags,
    })
