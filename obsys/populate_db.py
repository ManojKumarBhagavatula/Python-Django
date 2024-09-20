import os
import django
import sys

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'obsys.settings')  # Replace with your project name
django.setup()

from home.models import Tiffin, ColdDrink

def populate():
    tiffins = [
        {'name': 'Idly', 'price': 30.00},
        {'name': 'Dosa', 'price': 40.00},
        {'name': 'Vada', 'price': 25.00},
        {'name': 'Uttapam', 'price': 50.00},
        {'name': 'Ravva Dosa', 'price': 45.00},
        {'name': 'Masala Dosa', 'price': 55.00},
        {'name': 'Pongal', 'price': 35.00},
        {'name': 'Rawa Idly', 'price': 40.00},
        {'name': 'Set Dosa', 'price': 50.00},
        {'name': 'Cheese Dosa', 'price': 60.00},
    ]

    cold_drinks = [
        {'name': 'Cola', 'price': 20.00},
        {'name': 'Lemonade', 'price': 15.00},
        {'name': 'Orange Juice', 'price': 25.00},
        {'name': 'Mango Lassi', 'price': 30.00},
        {'name': 'Iced Tea', 'price': 18.00},
        {'name': 'Apple Juice', 'price': 22.00},
        {'name': 'Ginger Ale', 'price': 20.00},
        {'name': 'Pineapple Juice', 'price': 28.00},
        {'name': 'Sparkling Water', 'price': 15.00},
        {'name': 'Buttermilk', 'price': 10.00},
    ]

    for item in tiffins:
        Tiffin.objects.create(name=item['name'], price=item['price'])

    for item in cold_drinks:
        ColdDrink.objects.create(name=item['name'], price=item['price'])

if __name__ == '__main__':
    populate()
