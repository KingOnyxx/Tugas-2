from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)
    total=0
    for item in products:
        total+=item.Amount
    
    context = {
        'user':request.user.username,
        'Name': '',
        'Amount': '',
        'Price':'',
        'Category':'',
        'Publisher':'',
        'Description':'',
        'date_added':'',
        'total':total,
        'products': products,
        'last_login':request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            products = Product.objects.filter(user=request.user)
            
            for item in products:
                if item.Name== request.POST.get('Name'):
                    item.Amount += int(request.POST.get('Amount',0))
                    item.save()
                    return HttpResponseRedirect(reverse('main:show_main'))
            product.save()
            return HttpResponseRedirect(reverse('main:show_main'))
    context = {'form': form}
    return render(request, "create_product.html", context)
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    context = {}
    return render(request, 'login.html', context)
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
def update_amount(request, product_id):
    product = Product.objects.get(id=product_id)
    
    if request.method == "POST":
        if "increment" in request.POST:
            product.Amount += 1
            product.save()
        elif "decrement" in request.POST:
            product.Amount -= 1
            product.save()
            if product.Amount < 0:
                product.delete()
        elif "increment10" in request.POST:
            product.Amount += 10
            product.save()
        elif "decrement10" in request.POST:
            product.Amount -= 10
            product.save()
            if product.Amount < 0:
                product.delete()                
    
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
# Create your views here.