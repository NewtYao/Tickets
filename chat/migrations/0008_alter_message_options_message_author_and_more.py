# Generated by Django 5.0.6 on 2024-07-20 06:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_alter_message_options_alter_room_options_and_more'),
        ('website', '0008_alter_tickets_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='message',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='chatroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chat_message', to='chat.room'),
        ),
        migrations.AddField(
            model_name='message',
            name='content',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='room_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_chat', to='website.tickets'),
        ),
    ]
