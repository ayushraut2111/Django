# Generated by Django 4.2.4 on 2023-09-05 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0002_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
