# Generated by Django 4.2 on 2023-04-30 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_delete_room'),
    ]

    operations = [
        migrations.DeleteModel(
            name='student',
        ),
    ]