# Generated by Django 4.1.2 on 2022-10-07 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_author_author_pic_alter_blog_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_pic', models.ImageField(blank=True, null=True, upload_to='blog/user_pic/')),
                ('user_address', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=2000)),
                ('commented_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]