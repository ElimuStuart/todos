from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    done = models.BooleanField(default=False)
    
