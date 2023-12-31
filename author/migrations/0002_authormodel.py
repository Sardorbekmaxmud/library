# Generated by Django 4.2.3 on 2023-07-17 12:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(default='', max_length=100)),
                ('l_name', models.CharField(default='', max_length=100)),
                ('year_of_birth', models.DateField(default=datetime.datetime.now)),
                ('year_of_death', models.DateField(default=datetime.datetime.now, null=True)),
                ('birth_city_country', models.CharField(default='', max_length=100)),
                ('died_city_country', models.CharField(default='', max_length=100)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.categorymodel')),
            ],
        ),
    ]
