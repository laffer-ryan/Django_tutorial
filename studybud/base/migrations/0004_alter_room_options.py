# Generated by Django 4.2.6 on 2023-11-01 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_room_host'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ('-updated', '-created')},
        ),
    ]
