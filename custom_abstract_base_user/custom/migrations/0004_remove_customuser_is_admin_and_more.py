# Generated by Django 4.2.4 on 2023-09-05 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0003_rename_is_active_customuser_is_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_superuser',
        ),
    ]
