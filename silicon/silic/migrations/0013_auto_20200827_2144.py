# Generated by Django 3.1 on 2020-08-27 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silic', '0012_auto_20200824_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band_details',
            name='Clipart_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='band_order',
            name='Order_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
