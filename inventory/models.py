from django.db import models

# Create your models here.

class Product(models.Model):
    web_id = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=225)
    name = models.CharField(max_length=225)
    description = models.TextField(blank=True)
    is_activate =models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name