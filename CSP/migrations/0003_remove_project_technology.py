# Generated by Django 5.1 on 2024-09-09 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CSP', '0002_project_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='technology',
        ),
    ]
