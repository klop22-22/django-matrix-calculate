from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']


class Example(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    matrix_a = models.JSONField()
    matrix_b = models.JSONField(null=True, blank=True)
    operation = models.CharField(max_length=50)
    expected_result = models.JSONField()

    category = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        if self.category:
            return f"{self.category}, {self.name}"
        else:
            return self.name

    class Meta:
        verbose_name = 'Пример'
        verbose_name_plural = 'Примеры'
        ordering = ['created_at']    