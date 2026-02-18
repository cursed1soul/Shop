from django.urls import path
from .views import product_list, user_login, product_detail, product_delete

urlpatterns = [
    path('', user_login, name='login'), 
    path('products/', product_list, name='product_list'), 
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('products/<int:pk>/delete/', product_delete, name='product_delete'),
]


