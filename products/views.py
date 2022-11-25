from django.shortcuts import render
from django.http import HttpResponse
from .models import Products


def index(request):
    return render(request, "products/products.html")


def second_list(request):
    return HttpResponse("Second Page!")


def hello_sky_learn(request):
    return HttpResponse("Hello SkyLearn!")
