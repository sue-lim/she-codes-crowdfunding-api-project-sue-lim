# Generated by Django 4.1.5 on 2023-01-27 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_alter_comment_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(verbose_name='project_comment'),
        ),
    ]
