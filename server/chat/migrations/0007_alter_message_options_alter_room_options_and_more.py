# Generated by Django 5.0.6 on 2024-07-18 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_room_seller'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={},
        ),
        migrations.RemoveField(
            model_name='message',
            name='content',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sent_by',
        ),
        migrations.RemoveField(
            model_name='message',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='room',
            name='agent',
        ),
        migrations.RemoveField(
            model_name='room',
            name='client',
        ),
        migrations.RemoveField(
            model_name='room',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='room',
            name='messages',
        ),
        migrations.RemoveField(
            model_name='room',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='room',
            name='status',
        ),
        migrations.RemoveField(
            model_name='room',
            name='url',
        ),
        migrations.RemoveField(
            model_name='room',
            name='uuid',
        ),
    ]