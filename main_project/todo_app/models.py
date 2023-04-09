from django.db import models

class Todo(models.Model):

    todo = models.TextField()
    completed = models.BooleanField(default=False)
    todo_image = models.ImageField(upload_to="todos", null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.todo[:20]
    