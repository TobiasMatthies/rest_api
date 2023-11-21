from django.contrib import admin
from .models import Todo, User

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'id']

class UserAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Todo, TodoAdmin)
admin.site.register(User, UserAdmin)