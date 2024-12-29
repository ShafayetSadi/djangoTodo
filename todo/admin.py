from django.contrib import admin

from .models import Profile, Task

# Register your models here.
admin.site.register(Task)
admin.site.register(Profile)
