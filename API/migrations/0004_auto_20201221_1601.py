# Generated by Django 3.1.4 on 2020-12-21 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_auto_20201221_1558'),
    ]

    operations = [
        migrations.RenameField(
            model_name='headerimage',
            old_name='url',
            new_name='header_url',
        ),
    ]