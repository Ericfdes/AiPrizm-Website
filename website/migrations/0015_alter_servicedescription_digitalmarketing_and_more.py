# Generated by Django 4.1.1 on 2022-09-27 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_alter_contact_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicedescription',
            name='DigitalMarketing',
            field=models.TextField(default='none', max_length=500),
        ),
        migrations.AlterField(
            model_name='servicedescription',
            name='Mlearning',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='servicedescription',
            name='appdev',
            field=models.TextField(default='none', max_length=500),
        ),
        migrations.AlterField(
            model_name='servicedescription',
            name='automation',
            field=models.TextField(default='none', max_length=500),
        ),
        migrations.AlterField(
            model_name='servicedescription',
            name='dataA',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='servicedescription',
            name='headDiscription',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='servicedescription',
            name='webdev',
            field=models.TextField(max_length=500),
        ),
    ]