# Generated by Django 3.2.5 on 2021-07-22 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sumarga_app', '0009_auto_20210722_1820'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='image_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_name',
            new_name='name',
        ),
    ]
