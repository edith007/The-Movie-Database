# Generated by Django 2.2.12 on 2020-07-18 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20200717_1039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='plot',
        ),
        migrations.AddField(
            model_name='show',
            name='genres',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='show',
            name='image',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='show',
            name='name',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='userrating',
            name='position',
            field=models.IntegerField(default=0),
        ),
    ]
