from django.shortcuts import render, redirect, get_object_or_404 # Исправили опечатку тут
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Product

# 1. Окно входа
def user_login(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('product_list')
        else:
            messages.error(request, "Неверный логин или пароль")
    return render(request, 'shop/login.html')

# 2. Список товаров
def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

# 3. Детальная страница товара
def product_detail(request, pk):
    # Пытаемся найти товар по ID, если нет — выдаем 404 ошибку
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    # Проверка роли (если нужно)
    if request.user.is_authenticated and request.user.role.name == "Администратор":
        product.delete()
    return redirect('product_list')

