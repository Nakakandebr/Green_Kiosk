# Generated by Django 3.2.12 on 2023-09-01 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0002_vendor_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='image',
        ),
    ]
