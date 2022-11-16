# Generated by Django 3.2.12 on 2022-11-16 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.BooleanField(choices=[(True, 'Male'), (False, 'Female')])),
                ('description', models.TextField(max_length=250)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
