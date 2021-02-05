# Generated by Django 3.1 on 2020-08-21 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silic', '0010_auto_20200820_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category_product',
            name='Category_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='category_product',
            name='Discount_percentage',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='category_product',
            name='Maximum_quantity',
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='category_product',
            name='Minimum_quantity',
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='category_product',
            name='Product_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='category_product',
            name='Product_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='category_product',
            name='Status',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='category_product',
            name='Unit_price',
            field=models.FloatField(default=0, null=True),
        ),
    ]
