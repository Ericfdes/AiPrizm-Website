# Generated by Django 4.1.2 on 2022-10-08 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_comment_user_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user_pic',
            field=models.ImageField(default='../website/static/website/images/blog/test1.jpg', upload_to='blog/user_pic/'),
        ),
    ]