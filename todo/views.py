from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, UserForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def anonymous_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

@login_required
def index(request):
    context = {
        'tasks': Task.objects.filter(user=request.user),
    }
    # for task in context['tasks']:
    #     print(task.title)
    return render(request, 'todo/index.html', context)

def add_task(request):
    # handle this with htmx
    form = TaskForm(request.POST)
    if form.is_valid():
        # Save the task to the database
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        print("Task created successfully.")
        context = { 'task': task }
        return render(request, 'todo/index.html#task-partial', context)

def add(request):
    context = {
        'form': TaskForm(),
    }
    return render(request, 'todo/add_task.html', context)
    

def edit_task(request, task_id):
    form = TaskForm(request.POST)
    if form.is_valid():
        # edit the task given by task_id in the database
        task = Task.objects.get(id=task_id)
        task.title = form.cleaned_data['title']
        task.description = form.cleaned_data['description']
        task.due_date = form.cleaned_data['due_date']
        task.is_important = form.cleaned_data['is_important']
        task.save()
        context = { 'task': task }
    return redirect('index')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = True
    task.save()
    return redirect('index')

def profile(request):
    return render(request, 'todo/profile.html')

@anonymous_required
def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = User(
                username=user_form.cleaned_data['username'],
                email=user_form.cleaned_data['email'],
            )
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            print("User created successfully.")
            return redirect('login')
    user_form = UserForm()
    context = {
        'form': user_form,
    }
    return render(request, 'todo/register.html', context)