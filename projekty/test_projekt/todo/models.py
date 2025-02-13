from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=500, verbose_name='Description')

    is_finished = models.BooleanField(default=False)
    # blank = volitelné na úrovni UI
    # null = "volitelné" na úrovni DB
    finished_dt = models.DateTimeField(blank=True, null=True)
    dead_line_dt = models.DateTimeField(blank=True, null=True, verbose_name='Dead Line')
    
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

