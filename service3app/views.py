from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Products
from .serializers import ProductsSerializer

@api_view(['GET'])
def get_products(request):
    products = Products.objects.all()
    serializer = ProductsSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_product(request, code):
    try:
        product = Products.objects.get(code=code)
    except Products.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = ProductsSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_product(request):
    serializer = ProductsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def update_product(request, code):
    product = Products.objects.get(code=code)
    serializer = ProductsSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)