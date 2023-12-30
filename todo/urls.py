from django.urls import path
from . import views
from .forms import MyAuthForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add_task/', views.add_task, name='add_task'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='todo/login.html', authentication_form=MyAuthForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='todo/logout.html'), name='logout'),
]


"""
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)

path('login/', views.CustomLoginView.as_view(template_name='todo/login.html', authentication_form=MyAuthForm), name='login'),
"""