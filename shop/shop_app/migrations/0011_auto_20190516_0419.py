# Generated by Django 2.2.1 on 2019-05-16 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0010_tag_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='author',
        ),
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.ManyToManyField(to='shop_app.Author'),
        ),
    ]