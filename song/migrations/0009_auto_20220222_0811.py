# Generated by Django 3.2.7 on 2022-02-22 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0008_songfavorite'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='songfavorite',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='songreview',
            options={'ordering': ['-id']},
        ),
    ]
