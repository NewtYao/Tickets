# Generated by Django 5.0.6 on 2024-07-27 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_alter_message_author_alter_message_chatroom_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
