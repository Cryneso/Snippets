# Generated by Django 3.1 on 2021-11-17 09:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_auto_20211117_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]