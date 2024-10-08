from django.db import models

# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    genre = models.CharField(max_length=100, null=True, blank=True)
    internal_storage = models.CharField(max_length=10, null=True, blank=True)
    required_storage = models.CharField(max_length=10, null=True, blank=True)
    pre_owned = models.CharField(max_length=5, null=True, blank=True)
    colour = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    players = models.CharField(max_length=10, null=True, blank=True)
    age_rating = models.CharField(max_length=10, null=True, blank=True)
    star_rating = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    category = models.ForeignKey('Game', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    genre = models.CharField(max_length=100, null=True, blank=True)
    required_storage = models.CharField(max_length=10, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    players = models.CharField(max_length=10, null=True, blank=True)
    age_rating = models.CharField(max_length=10, null=True, blank=True)
    star_rating = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)

class Console(models.Model):
    category = models.ForeignKey('Console', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    internal_storage = models.CharField(max_length=10, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    star_rating = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)

class Accessories(models.Model):
    category = models.ForeignKey('Accessories', null=True, blank=True, on_delete=models.SET_NULL)
    colour = models.CharField(max_length=50, null=True, blank=True)

