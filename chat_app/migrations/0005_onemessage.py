# Generated by Django 2.0 on 2018-09-07 10:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0004_oneroom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Onemessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.TextField(blank=True)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='onemessages', to='chat_app.Oneroom')),
            ],
        ),
    ]
