from django.db import models

class Product(models.Model):
    Name = models.CharField(max_length=255)
    Amount=models.IntegerField()
    Price = models.DecimalField(max_digits=5, decimal_places=2)
    Category=models.TextField()
    Publisher=models.TextField()
    Description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
# Create your models here.
