# Generated by Django 4.1.2 on 2022-10-09 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_author_linkedin_author_stack_overflow_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='facebook',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='instagram',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='linkedin',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='stack_overflow',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='twitter',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
