from django.urls import path

from .views import ProductListCreate, index


urlpatterns = [
    path('', index, name='home'),
    path('api/products/', ProductListCreate.as_view(),
         name='product-list-create'
         ),
]
