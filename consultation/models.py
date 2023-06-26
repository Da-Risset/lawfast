from django.db import models
from django.contrib.auth.models import User


class Lawyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='lawyer')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='lawyer/images', default='lawyer/images/default.png')
    specialization = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    description = models.TextField()
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Review(models.Model):
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.review


class Consultation(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Completed', 'Completed'),
    )
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE, related_name='consultations')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='consultations')
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    duration = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.description