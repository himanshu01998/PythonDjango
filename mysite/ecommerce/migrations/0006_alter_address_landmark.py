# Generated by Django 4.0.1 on 2022-01-19 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_contact_alter_cart_quantity_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='landmark',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
