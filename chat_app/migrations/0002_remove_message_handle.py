# Generated by Django 2.0 on 2018-09-03 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='handle',
        ),
    ]
