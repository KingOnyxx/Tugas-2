from django.shortcuts import render
def show_main(request):
    context = {
        'app':'Skin Bundle Inventory',
        'name': 'Prime',
        'amount': '5',
        'desc':'Classic, Spectre, Guardian, Vandal, Melee',
        'price':'7,100 VP',
        'category':'Bundle'

    }

    return render(request, "main.html", context)
# Create your views here.
