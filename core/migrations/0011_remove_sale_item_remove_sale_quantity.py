# Generated by Django 4.2 on 2025-04-29 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_sale_item_sale_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='item',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='quantity',
        ),
    ]
