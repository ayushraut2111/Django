# Generated by Django 4.2 on 2023-04-30 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_remove_student_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentone',
            name='course',
        ),
    ]
