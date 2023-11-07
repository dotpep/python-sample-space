# Generated by Django 4.2.6 on 2023-11-07 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('contact', models.CharField(max_length=20, verbose_name='Phone number')),
                ('date_time', models.DateTimeField()),
                ('count_quest', models.IntegerField()),
                ('notes', models.TextField(blank=True, max_length=300)),
            ],
        ),
    ]
