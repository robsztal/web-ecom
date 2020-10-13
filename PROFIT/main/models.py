from django.db import models


class Storage(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    quantity = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return self.name
