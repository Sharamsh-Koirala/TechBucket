# Generated by Django 4.0.5 on 2022-09-20 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_partner'),
    ]

    operations = [
        migrations.AddField(
            model_name='customertestimonial',
            name='name',
            field=models.CharField(default='default', max_length=200),
            preserve_default=False,
        ),
    ]
