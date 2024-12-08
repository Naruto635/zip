from django.contrib import admin
from .models import Goal, Task, Profile

admin.site.register(Profile)
admin.site.register(Goal)
admin.site.register(Task)
