# Generated by Django 4.1.1 on 2022-09-26 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_rename_phone_contact_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
