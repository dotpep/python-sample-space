# Generated by Django 4.2.6 on 2023-11-12 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('vendor', models.CharField(choices=[('tefal', 'Tefal'), ('fissman', 'Fissman')], max_length=128)),
                ('diameter', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
