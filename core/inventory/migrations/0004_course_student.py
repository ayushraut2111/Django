# Generated by Django 4.2 on 2023-04-30 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_product_colour'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('course_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('roll_number', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.course')),
            ],
        ),
    ]