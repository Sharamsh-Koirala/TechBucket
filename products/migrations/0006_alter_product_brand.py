# Generated by Django 4.0.5 on 2022-06-30 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_brand_product_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.brand'),
        ),
    ]