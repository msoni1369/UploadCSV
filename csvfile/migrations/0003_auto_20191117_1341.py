# Generated by Django 2.2.4 on 2019-11-17 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csvfile', '0002_auto_20191116_1759'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='username',
        ),
    ]