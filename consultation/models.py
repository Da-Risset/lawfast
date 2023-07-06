from django.db import models
from django.contrib.auth.models import User, Group
from django.core.files.base import ContentFile
from io import BytesIO
from PIL import Image


class Lawyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='lawyer')
    group = models.CharField(max_length=100, default='Lawyer', blank=True, null=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='lawyer/images', default='lawyer/images/default.jpg', blank=True, null=True)
    specialization = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    description = models.TextField()
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk is None:
            super(Lawyer, self).save()
            lawyer_group = Group.objects.get(name='Lawyer')
            self.user.groups.add(lawyer_group)

        if self.image:
            img = Image.open(self.image)
            if img.width > 719 or img.height > 675:
                output_size = (719, 675)

                img.thumbnail(output_size)
                in_mem_file = BytesIO()
                img.save(in_mem_file, format='JPEG')
                in_mem_file.seek(0)

                self.image.save(self.image.name, ContentFile(in_mem_file.read()), save=False)
                in_mem_file.close()

        super(Lawyer, self).save()


class Review(models.Model):
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.review


class Consultation(models.Model):
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE, related_name='consultations')
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lawyer.name


class Variation(models.Model):

    TYPE_CHOICES = (
        ('Chat', 'Chat'),
        ('Call', 'Call'),
        ('Meet', 'Meet'),
    )

    DURATION_CHOICES = (
        (15, '15 minutes'),
        (30, '30 minutes'),
        (45, '45 minutes'),
        (60, '1 hour'),
    )

    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, related_name='variations')
    description = models.TextField(blank=True, null=True)
    # duration minutes
    duration = models.PositiveIntegerField(choices=DURATION_CHOICES, blank=True, null=True)
    # type of consultation
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, blank=True, null=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.description

    def get_type(self):
        return self.type

    def get_duration(self):
        return self.duration

    def save(self, *args, **kwargs):
        if self.type and self.duration and self.price:
            self.description = f'{self.type} consultation for {self.duration} minutes at {self.price} rupiah'
        elif self.type and self.duration:
            self.description = f'{self.type} consultation for {self.duration} minutes'
        elif self.type and self.price:
            self.description = f'{self.type} consultation at {self.price} rupiah'
        elif self.duration and self.price:
            self.description = f'Consultation for {self.duration} minutes at {self.price} rupiah'
        elif self.type:
            self.description = f'{self.type} consultation'
        elif self.duration:
            self.description = f'Consultation for {self.duration} minutes'
        elif self.price:
            self.description = f'Consultation at {self.price} rupiah'
        else:
            self.description = 'Consultation'

        super(Variation, self).save(*args, **kwargs)
