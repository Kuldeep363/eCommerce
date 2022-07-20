# Generated by Django 4.0.6 on 2022-07-20 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_product_color_alter_product_countryoforigin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='prodImages',
        ),
        migrations.AddField(
            model_name='product',
            name='prodImages',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productImage', to='store.images'),
        ),
    ]
