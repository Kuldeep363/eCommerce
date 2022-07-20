# Generated by Django 4.0.6 on 2022-07-20 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_product_prodimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(default='black', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='countryOfOrigin',
            field=models.CharField(default='India', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='null'),
        ),
    ]
