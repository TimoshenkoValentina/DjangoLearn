from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=50)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=100, unique=True)
