from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("Hello, world.")


def zipsearch(request):
    return HttpResponse(request.get_full_path())