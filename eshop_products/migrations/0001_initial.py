# Generated by Django 4.1.5 on 2023-01-30 18:09

from django.db import migrations, models
import eshop_products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=eshop_products.models.upload_image_path)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
