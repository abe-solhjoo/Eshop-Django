import os.path

from django.db import models


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f'{instance.id}-{instance.title}{ext}'
    return f"products/{final_name}"


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
