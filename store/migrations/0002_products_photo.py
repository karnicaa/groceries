# Generated by Django 3.1.7 on 2021-04-06 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='photo',
            field=models.ImageField(default=True, upload_to='images'),
        ),
    ]