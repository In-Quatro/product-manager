from django.core.exceptions import ValidationError
from django.shortcuts import render
from rest_framework import generics

from .serializers import ProductSerializer
from .models import Product


class ProductListCreate(generics.ListCreateAPIView):
    """View для отображения списка продуктов и создания нового продукта."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        price = serializer.validated_data.get('price')
        if price <= 0:
            raise ValidationError(
                "Цена должна быть положительным числом."
            )
        serializer.save()


def index(request):
    """Функция для отображения шаблона."""
    return render(request, 'index.html')
