from django.db import models

class Product(models.Model):
    app = models.TextField()
    name = models.CharField(max_length=255)
    amount=models.IntegerField()
    desc = models.TextField()
    price = models.IntegerField()
    cat=models.TextField()
    pub=models.TextField()
    

# Create your models here.
