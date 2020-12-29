# Generated by Django 3.1.4 on 2020-12-29 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0021_auto_20201228_2124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(related_name='books_genres', to='manager.Genre'),
        ),
    ]