from django.shortcuts import render
def show_main(request):
    context = {
        'app':'Cuci Cuci Service',
        'name': 'Clarence Grady',
        'class': 'PBP A'

    }

    return render(request, "main.html", context)
# Create your views here.
