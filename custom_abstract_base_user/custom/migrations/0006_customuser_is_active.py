# Generated by Django 4.2.4 on 2023-09-05 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0005_customuser_is_staff_customuser_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
