# Generated by Django 2.2 on 2019-04-27 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0006_auto_20190427_1920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='author',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]