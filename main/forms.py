from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["Name", "Amount", "Price", "Category","Publisher", "Description",]