# Generated by Django 4.2.6 on 2023-12-08 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
