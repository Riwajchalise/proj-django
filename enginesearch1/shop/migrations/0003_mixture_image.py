# Generated by Django 2.0.1 on 2018-07-10 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20180710_0615'),
    ]

    operations = [
        migrations.AddField(
            model_name='mixture',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
    ]
