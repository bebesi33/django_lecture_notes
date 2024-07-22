from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello World!")


def home_with_template(request):
    return render(request, 'home.html', {'additonal_message': 'Hello László!'})
