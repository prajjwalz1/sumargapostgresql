# Generated by Django 3.2.5 on 2021-07-17 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sumarga_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='image_home',
            new_name='img',
        ),
    ]
