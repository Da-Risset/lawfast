# Generated by Django 4.1.4 on 2023-07-06 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0003_alter_lawyer_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lawyer',
            name='image',
            field=models.ImageField(blank=True, default='lawyer/images/default.png', null=True, upload_to='lawyer/images'),
        ),
    ]
