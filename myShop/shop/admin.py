from django.contrib import admin
from .models import Role, User, Product, Order

# Регистрация моделей в админ-панели
admin.site.register(Role)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)
