from django.db import models

# Create your models here.
class Products(models.Model):
    code = models.CharField(max_length=20)
    purchase_price = models.IntegerField()
    sale_price = models.IntegerField()
    description = models.TextField()