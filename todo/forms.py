from django import forms
from django.contrib.auth.models import User
from todo.models import Task, Profile
from django.forms.widgets import TextInput, DateInput
from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit
from crispy_tailwind.layout import Submit, Button, Reset
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm

class MyAuthForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs=
        {
            'class': 'textinput block w-full bg-[#121212] rounded-lg px-4 py-2 border-transparent focus:border-transparent focus:ring-0',
            'placeholder': 'username',
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(attrs=
        {
            'class': 'textinput block w-full bg-[#121212] rounded-lg px-4 py-2 border-transparent focus:border-transparent focus:ring-0',
            'placeholder': 'password',
            }
    ))


class TaskForm(forms.ModelForm):
    # title = forms.CharField(
    #     widget=forms.TextInput(attrs={
    #     'placeholder': "Add new task...",
    #     'class': 'textinput block w-full bg-[#121212] rounded-lg px-4 py-2 border-transparent focus:border-transparent focus:ring-0',
    # }))
    # description = forms.CharField(widget=forms.Textarea(
    #     attrs={
    #         'placeholder': "Add description...",
    #         'cols': "40",
    #         'rows': "6",
    #         'class': "resize-none textarea block w-full border bg-[#121212] rounded-lg appearance-none px-4 py-2 border-transparent focus:border-transparent focus:ring-0"
    #     }))
    # due_date = forms.DateField(widget=forms.DateInput(
    #     attrs={
    #         'type': 'date',
    #         'class': "dateinput block w-full border bg-[#121212] rounded-lg appearance-none px-4 py-2 border-transparent focus:border-transparent focus:ring-0"
    #     }))
    # is_important = forms.BooleanField(
    #         required=False,
    #         widget=forms.CheckboxInput(
    #             attrs={
    #                 'class': "form-checkbox m-2 h-5 w-5 text-gray-600 border-transparent focus:border-transparent focus:ring-0"
    #             }
    #         )
    #     )
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'is_important']
        widgets = {
            'title': TextInput(attrs={
                'placeholder': "Add new task...",
                'class': 'textinput block w-full bg-[#121212] rounded-lg px-4 py-2 border-transparent focus:border-transparent focus:ring-0',
            }),
            'description': TextInput(attrs={
                'placeholder': "Add description...",
                'class': "resize-none textarea block w-full border bg-[#121212] rounded-lg appearance-none px-4 py-2 border-transparent focus:border-transparent focus:ring-0",
            }),
            'due_date': DateInput(attrs={
                'type': 'date',
                'class': "dateinput block w-full border bg-[#121212] rounded-lg appearance-none px-4 py-2 border-transparent focus:border-transparent focus:ring-0"
            }),
            'is_important': forms.CheckboxInput(
                attrs={
                    'class': "form-checkbox m-2 h-5 w-5 text-gray-600 border-transparent focus:border-transparent focus:ring-0"
                }
            )
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic']

