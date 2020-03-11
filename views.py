from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return HttpResponse("We are at about.")

def tracker(request):
    return HttpResponse("We are at tracker.")

def contact(request):
     return HttpResponse("We are at contact.")

def productView(request):
     return HttpResponse("We are at proddslfklf.")

def search(request):
     return HttpResponse("We are at search.")

def checkout(request):
    return HttpResponse("This is your cart")     