from django.db import models
from users.models import CustomUser

class Todo(models.Model):
    label = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)
    owner = models.ForeignKey(CustomUser, related_name='todos', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now=False, null=True, blank=True)

    class Meta:
        db_table = 'todos'
        ordering = ['created_at']
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'