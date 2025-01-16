from django.db import models

# Create your models here.
class Todolist(models.Model):
    title = models.CharField(max_length=10)
    description = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    time_of_completion = models.DateTimeField(null=True, blank=True)

