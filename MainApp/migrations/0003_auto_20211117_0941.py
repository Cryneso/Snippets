# Generated by Django 3.1 on 2021-11-17 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_snippet_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='rate',
        ),
    ]
