# Generated by Django 3.1 on 2020-08-18 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silic', '0004_registration_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band_details',
            name='Clipart_image',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='category_product',
            name='Discount_percentage',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='category_product',
            name='Maximum_quantity',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='category_product',
            name='Minimum_quantity',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='category_product',
            name='Unit_price',
            field=models.FloatField(default=0),
        ),
    ]