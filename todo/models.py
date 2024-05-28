from django.db import models

# Create your models here.
from django.conf import settings
from django.urls import reverse


class Todo(models.Model):
    author = models.ForeignKey(
        #'auth.User',
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )
    title = models.CharField(max_length=150, unique=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
    time_to_start = models.DateTimeField(null=True, blank=True)
    time_to_finish = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('todo_detail', kwargs={'pk':self.pk})