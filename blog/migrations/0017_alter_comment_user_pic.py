# Generated by Django 4.1.2 on 2022-10-08 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_comment_user_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user_pic',
            field=models.ImageField(blank=True, default='/home/valiantdoge/Documents/Code/eric/AiPrizm-Website/website/static/website/images/blog/test1.jpg', null=True, upload_to='blog/user_pic/'),
        ),
    ]
