# Generated by Django 4.0.5 on 2022-06-30 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_brand_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.brand'),
            preserve_default=False,
        ),
    ]
