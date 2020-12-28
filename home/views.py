from django.shortcuts import render
from home.models import HomePage

def index(request):
    home = HomePage.objects.first()
    print(f"home name {home.name}")
    context = {}
    context['name'] = home.name
    return render(request, 'home/home_page.html', context)
