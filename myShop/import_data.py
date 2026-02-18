import os
import django
import pandas as pd

# Настройка окружения Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from shop.models import Product

def import_products(file_path):
    if not os.path.exists(file_path):
        print(f"Ошибка: Файл {file_path} не найден!")
        return

    # Читаем Excel
    df = pd.read_excel(file_path)
    
    print("Начинаю импорт...")
    for index, row in df.iterrows():
        try:
            # Используем update_or_create, чтобы обновить существующие товары картинками
            obj, created = Product.objects.update_or_create(
                title=row['Наименование товара'], 
                defaults={
                    'description': row['Описание товара'],
                    'price': row['Цена'],
                    'quantity': row['Кол-во на складе'],
                    'image': f"products/{row['Фото']}" # Путь к фото
                }
            )
            if created:
                print(f"Добавлен: {row['Наименование товара']}")
            else:
                print(f"Обновлен: {row['Наименование товара']}")
                
        except Exception as e:
            print(f"Ошибка на строке {index}: {e}")
            
    print("\n--- Импорт завершен! Проверь сайт. ---")

if __name__ == "__main__":
    import_products('Tovar.xlsx')
