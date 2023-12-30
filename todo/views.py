from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, UserForm, ProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def anonymous_required(view_func):
    @login_required
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
    # if request.method == 'POST':
    #     form = TaskForm(request.POST)
    #     if form.is_valid():
    #         # Save the task to the database
    #         task = form.save(commit=False)
    #         task.user = request.user
    #         task.save()
    #         print("Task created successfully.")
    #         return redirect('index')
    # else:
    #     context = {
    #         'form': TaskForm(),
    #     }
    # return render(request, 'todo/add_task.html', context)

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
    return render(request, 'todo/edit_task.html')

def delete_task(request, task_id):
    return render(request, 'todo/delete_task.html')

def complete_task(request, task_id):
    return render(request, 'todo/complete_task.html')

def profile(request):
    return render(request, 'todo/profile.html')

@anonymous_required
def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            # Hash the password
            user.set_password(user.password)
            user.save()
            print("User created successfully.")
            return redirect('login')
    else:
        user_form = UserForm()
        context = {
            'form': user_form,
        }
    return render(request, 'todo/register.html', context)