# Generated by Django 4.2 on 2023-04-30 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_studentone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='room',
        ),
    ]
