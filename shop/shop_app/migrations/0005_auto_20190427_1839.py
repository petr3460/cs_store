# Generated by Django 2.2 on 2019-04-27 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0004_possibleproductattributes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Brand',
            new_name='Owner',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='logo',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='brand',
            new_name='owner',
        ),
        migrations.AlterField(
            model_name='attribute',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='measure',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]