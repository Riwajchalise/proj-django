# Generated by Django 2.0.5 on 2018-07-18 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_auto_20180718_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
    ]
