# Generated by Django 2.2.5 on 2020-01-20 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20200120_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]