# Generated by Django 4.1.4 on 2023-07-06 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
