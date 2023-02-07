# Generated by Django 4.1.5 on 2023-02-07 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0004_productgallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productgallery',
            options={'verbose_name': 'گالری', 'verbose_name_plural': 'گالری ها'},
        ),
        migrations.AlterField(
            model_name='productgallery',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop_products.product', verbose_name='محصول'),
        ),
    ]