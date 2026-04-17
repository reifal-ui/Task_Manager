from django.db import models
from datetime import datetime

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add= True)
    end_date = models.DateTimeField(auto_now_add=False)
    def is_end_date(self):
        return datetime.now > self.end_date