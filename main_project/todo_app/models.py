from django.db import models

class Todo(models.Model):

    todo = models.TextField()
    completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)