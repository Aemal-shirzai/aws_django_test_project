# Generated by Django 4.2 on 2023-04-09 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_todo_todo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='todo_image',
            field=models.ImageField(null=True, upload_to='main_project/my_images'),
        ),
    ]
