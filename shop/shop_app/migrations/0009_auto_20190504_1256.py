# Generated by Django 2.2 on 2019-05-04 09:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop_app', '0008_auto_20190428_1446'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Review',
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'отзыв', 'verbose_name_plural': 'отзывы'},
        ),
    ]
