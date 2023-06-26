from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Published', 'Published'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/images', default='articles/images/default.png')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Draft')

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
