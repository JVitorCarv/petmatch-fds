# Generated by Django 4.0.4 on 2022-05-24 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petmatchapp', '0002_petprofile_pet_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petprofile',
            name='pet_image',
            field=models.ImageField(upload_to='pet_image'),
        ),
    ]
