# Generated by Django 4.0.6 on 2022-07-20 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_remove_product_prodimages_product_prodimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='prodImages',
        ),
        migrations.AddField(
            model_name='product',
            name='prodImages',
            field=models.ManyToManyField(blank=True, null=True, related_name='productImage', to='store.images'),
        ),
    ]
