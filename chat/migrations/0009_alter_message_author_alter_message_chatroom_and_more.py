# Generated by Django 5.0.6 on 2024-07-20 06:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_alter_message_options_message_author_and_more'),
        ('website', '0008_alter_tickets_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='chatroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_message', to='chat.room'),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket_chat', to='website.tickets'),
        ),
    ]
