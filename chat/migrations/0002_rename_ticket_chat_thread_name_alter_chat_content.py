# Generated by Django 5.0.6 on 2024-07-13 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='ticket',
            new_name='thread_name',
        ),
        migrations.AlterField(
            model_name='chat',
            name='content',
            field=models.TextField(max_length=2000),
        ),
    ]
