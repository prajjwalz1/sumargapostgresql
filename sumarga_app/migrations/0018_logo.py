# Generated by Django 3.2.5 on 2021-09-29 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sumarga_app', '0017_images_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='pic')),
            ],
        ),
    ]
