# Generated by Django 4.2 on 2023-04-09 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='todo_image',
            field=models.ImageField(null=True, upload_to='my_images'),
        ),
    ]
