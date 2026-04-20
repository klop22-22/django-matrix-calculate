from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    extra = models.CharField(max_length=200)
    
    def __str__(self):
        return self.username

class UserHistory(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    matrix_a = models.JSONField()
    matrix_b = models.JSONField(null=True, blank=True)
    operation = models.CharField(max_length=50)
    result = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='history')

    def __str__(self):
        return f"{self.user.username} - {self.operation} - {self.created_at}"

    class Meta:
        verbose_name = 'История вычислений'
        verbose_name_plural = 'История вычислений'
        ordering = ['-created_at']