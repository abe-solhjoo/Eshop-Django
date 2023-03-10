# Generated by Django 4.1.5 on 2023-02-03 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0002_alter_product_options_alter_product_active_and_more'),
        ('eshop_tag', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'برچسب', 'verbose_name_plural': 'برچسب ها'},
        ),
        migrations.AlterField(
            model_name='tag',
            name='active',
            field=models.BooleanField(default=True, verbose_name='فعال'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='products',
            field=models.ManyToManyField(blank=True, to='eshop_products.product', verbose_name='محصولات'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(verbose_name='اسلاگ'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=120, verbose_name='عنوان'),
        ),
    ]
