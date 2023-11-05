# Generated by Django 4.2.6 on 2023-11-05 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0002_rename_name_person_nickname_person_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('1', 'Civil'), ('2', 'Electrical'), ('3', 'Mechanical'), ('4', 'CompSci')], default='1', max_length=20)),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.CharField(default='Mumbai', max_length=50),
        ),
        migrations.AddField(
            model_name='person',
            name='tax_code',
            field=models.IntegerField(max_length=20, null=True, unique=True),
        ),
    ]