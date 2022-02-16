# Generated by Django 3.2 on 2022-02-16 21:01

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualbookshelf2022', '0007_auto_20220216_2100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='book_image',
        ),
        migrations.AddField(
            model_name='post',
            name='featured_image_cloud',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
