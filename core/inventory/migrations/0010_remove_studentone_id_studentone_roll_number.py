# Generated by Django 4.2 on 2023-04-30 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_remove_studentone_roll_number_studentone_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentone',
            name='id',
        ),
        migrations.AddField(
            model_name='studentone',
            name='roll_number',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
