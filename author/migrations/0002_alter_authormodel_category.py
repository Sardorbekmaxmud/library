# Generated by Django 4.2.3 on 2023-07-18 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authormodel',
            name='category',
            field=models.ManyToManyField(to='category.categorymodel'),
        ),
    ]
