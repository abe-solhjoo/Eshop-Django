# Generated by Django 4.1.5 on 2023-02-03 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products_category', '0002_alter_productcategory_options'),
        ('eshop_products', '0002_alter_product_options_alter_product_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, to='eshop_products_category.productcategory', verbose_name='دسته بندی ها'),
        ),
    ]
