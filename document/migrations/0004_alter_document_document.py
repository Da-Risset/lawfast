# Generated by Django 4.2.3 on 2023-07-07 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0003_typedocument_remove_document_type_document_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='documents'),
        ),
    ]
