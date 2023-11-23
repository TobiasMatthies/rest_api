from django.contrib import admin
from .models import Todo, User

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'id']
    
admin.site.register(Todo, TodoAdmin)