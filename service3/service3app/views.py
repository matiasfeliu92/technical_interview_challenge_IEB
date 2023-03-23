from django.http import JsonResponse
from django.shortcuts import render
from .models import Products

# Create your views here.
def getProducts(request):
    products = Products.objects.all().values()
    print(products)
    return JsonResponse([dict(row) for row in products])