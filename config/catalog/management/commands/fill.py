# from django.core.management import BaseCommand
# from catalog.models import Product
#
#
# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         products_list = [
#             {
#                 "title": "помидор",
#                 "description": "овощи свежие",
#                 "image": "",
#                 "category_id": 8,
#                 "purchase_price": "10.00"
#             },
#             {
#                 "title": "яблоко",
#                 "description": "фрукты свежие",
#                 "image": "",
#                 "category_id": 10,
#                 "purchase_price": "15.00"
#             },
#             {
#                 "title": "стул",
#                 "description": "мебель класическая",
#                 "image": "",
#                 "category_id": 9,
#                 "purchase_price": "55.00"
#             },
#             {
#                 "title": "джинсы",
#                 "description": "одежда из европы",
#                 "image": "",
#                 "category_id": 10,
#                 "purchase_price": "15.00"
#             }
#         ]
#
#         products_for_create = []
#
#         for products_item in products_list:
#             products_for_create.append(
#                 Product(**products_item)
#             )
#         Product.objects.bulk_create(products_for_create)
from django.core.management.base import BaseCommand
from catalog.models import Product


class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Удаление старых данных...')
        Product.objects.all().delete()
        self.stdout.write('Старые данные удалены.')

        self.stdout.write('Наполнение базы новыми данными...')
        products_list = [
            {
                "title": "помидор",
                "description": "овощи свежие",
                "image": "",
                "category_id": 8,
                "purchase_price": "10.00"
            },
            {
                "title": "яблоко",
                "description": "фрукты свежие",
                "image": "",
                "category_id": 10,
                "purchase_price": "15.00"
            },
            {
                "title": "стул",
                "description": "мебель класическая",
                "image": "",
                "category_id": 9,
                "purchase_price": "55.00"
            },
            {
                "title": "джинсы",
                "description": "одежда из европы",
                "image": "",
                "category_id": 10,
                "purchase_price": "15.00"
            },
            {
                "title": "кепка",
                "description": "одежда из европы",
                "image": "",
                "category_id": 10,
                "purchase_price": "25.00"
            }
        ]

        products_for_create = [
            Product(**product_data) for product_data in products_list
        ]
        Product.objects.bulk_create(products_for_create)

        self.stdout.write(self.style.SUCCESS('База данных заполнена новыми данными.'))
