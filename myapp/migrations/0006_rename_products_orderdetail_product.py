# Generated by Django 4.0 on 2024-07-10 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_orderdetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetail',
            old_name='products',
            new_name='product',
        ),
    ]