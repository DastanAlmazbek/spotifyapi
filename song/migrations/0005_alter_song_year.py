# Generated by Django 3.2.7 on 2022-02-18 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0004_alter_song_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='year',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
