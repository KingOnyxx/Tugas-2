from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=255)
    Amount=models.IntegerField()
    Price = models.DecimalField(max_digits=5, decimal_places=2)
    Category=models.TextField()
    Publisher=models.TextField()
    Description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
# Create your models here.
