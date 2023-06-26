from django.db import models
from django.contrib.auth.models import User
from consultation.models import Lawyer


class Document(models.Model):
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE, related_name='documents')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(max_length=100)
    document = models.FileField(upload_to='documents')
    description = models.TextField()

    published = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title