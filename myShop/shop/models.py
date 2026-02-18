from django.db import models
from django.contrib.auth.models import AbstractUser

# 1. Таблица Ролей (для нормализации)
class Role(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название роли")
    
    def __str__(self):
        return self.name

# 2. Таблица Пользователей (с привязкой к роли)
class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)

# 3. Таблица Товаров
class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    quantity = models.IntegerField(default=0, verbose_name="Остаток")
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.title

# 4. Таблица Заказов
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Заказчик")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа")
    status = models.CharField(max_length=50, default="Новый")

    def __str__(self):
        return f"Заказ №{self.id} от {self.user.username}"
