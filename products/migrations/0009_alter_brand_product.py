# Generated by Django 4.0.5 on 2022-06-30 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_remove_product_brand_brand_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product'),
        ),
    ]
