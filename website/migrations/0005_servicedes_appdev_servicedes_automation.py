# Generated by Django 4.1.1 on 2022-09-24 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_servicedes'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicedes',
            name='appdev',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='servicedes',
            name='automation',
            field=models.CharField(default='none', max_length=100),
        ),
    ]