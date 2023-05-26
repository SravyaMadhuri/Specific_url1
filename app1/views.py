from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def csk(request):
    return HttpResponse('<h1> THIS IS THE FISRT APP1 SPECIFIC URL MAPPING </h1>')