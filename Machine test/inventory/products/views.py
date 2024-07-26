from django.shortcuts import render
# products/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Products, Variants, SubVariants
from .serializers import ProductSerializer, VariantSerializer, SubVariantSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class AddStockView(viewsets.ViewSet):
    def create(self, request):
        variant_id = request.data.get('variant_id')
        quantity = request.data.get('quantity')

        try:
            subvariant = SubVariants.objects.get(id=variant_id)
            subvariant.stock += quantity
            subvariant.save()
            return Response({'status': 'Stock added'}, status=status.HTTP_200_OK)
        except SubVariants.DoesNotExist:
            return Response({'error': 'SubVariant not found'}, status=status.HTTP_404_NOT_FOUND)

class RemoveStockView(viewsets.ViewSet):
    def create(self, request):
        variant_id = request.data.get('variant_id')
        quantity = request.data.get('quantity')

        try:
            subvariant = SubVariants.objects.get(id=variant_id)
            if subvariant.stock >= quantity:
                subvariant.stock -= quantity
                subvariant.save()
                return Response({'status': 'Stock removed'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Insufficient stock'}, status=status.HTTP_400_BAD_REQUEST)
        except SubVariants.DoesNotExist:
            return Response({'error': 'SubVariant not found'}, status=status.HTTP_404_NOT_FOUND)

