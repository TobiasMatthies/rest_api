from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title