# Generated by Django 2.2.5 on 2020-01-21 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20200120_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='menu_items',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='pizzas',
        ),
        migrations.CreateModel(
            name='Cart_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=50)),
                ('toppings', models.CharField(max_length=50)),
                ('qty', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='pages.Cart')),
            ],
        ),
    ]
