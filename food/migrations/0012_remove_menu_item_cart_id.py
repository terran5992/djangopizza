# Generated by Django 2.2.5 on 2020-01-20 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0011_menu_item_cart_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu_item',
            name='cart_id',
        ),
    ]
