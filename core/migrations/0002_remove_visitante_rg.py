# Generated by Django 4.2.20 on 2025-03-13 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitante',
            name='rg',
        ),
    ]
