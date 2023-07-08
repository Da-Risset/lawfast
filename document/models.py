from django.db import models
from django.contrib.auth.models import User
from consultation.models import Lawyer


class TypeDocument(models.Model):
    TYPE_CHOICES = (
        ("Surat Kuasa", "Surat Kuasa"),
        ("Surat Gugatan", "Surat Gugatan"),
        ("Surat Perjanjian", "Surat Perjanjian"),
        ("Kontrak Kerja", "Kontrak Kerja"),
    )
    name = models.CharField(max_length=20, choices=TYPE_CHOICES, default='Surat Kuasa')

    def __str__(self):
        return self.name


class Document(models.Model):
    TYPE_CHOICES = (
        ("Surat Kuasa", "Surat Kuasa"),
        ("Surat Gugatan", "Surat Gugatan"),
        ("Surat Perjanjian", "Surat Perjanjian"),
        ("Kontrak Kerja", "Kontrak Kerja"),
    )

    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE, related_name='documents')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(max_length=100)
    type = models.ForeignKey(TypeDocument, on_delete=models.CASCADE, related_name='documents', blank=True, null=True)
    document = models.FileField(upload_to='documents', blank=True, null=True)
    description = models.TextField()
    price = models.PositiveIntegerField(blank=True, null=True)
    verified = models.BooleanField(default=False)

    published = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_price(self):
        return self.price