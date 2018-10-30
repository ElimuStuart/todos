from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    due_date = models.DateField()
    done = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return self.title
    
