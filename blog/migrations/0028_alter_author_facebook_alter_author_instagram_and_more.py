# Generated by Django 4.1.2 on 2022-10-09 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_author_author_prof_alter_author_author_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='facebook',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='author',
            name='instagram',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='author',
            name='twitter',
            field=models.CharField(max_length=200),
        ),
    ]