# Generated by Django 4.1.2 on 2022-10-09 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_alter_comment_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_comments', to='blog.blog'),
        ),
    ]
