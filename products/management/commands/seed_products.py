from django.core.management.base import BaseCommand
from products.models import Product, Category

class Command(BaseCommand):
    help = "Seed demo categories and products"

    def handle(self, *args, **kwargs):
        cats = [
            ("Papeterie", "papeterie"),
            ("Informatique", "informatique"),
        ]
        obj = {}
        for name, slug in cats:
            obj[slug], _ = Category.objects.get_or_create(name=name, slug=slug)

        data = [
            {"name": "Crayon", "price": "1.50", "stock": 10, "category": obj["papeterie"]},
            {"name": "Cahier", "price": "3.20", "stock": 5, "category": obj["papeterie"]},
            {"name": "Souris", "price": "12.90", "stock": 2, "category": obj["informatique"]},
        ]
        for d in data:
            Product.objects.get_or_create(name=d["name"], defaults={
                "price": d["price"], "stock": d["stock"], "category": d["category"],
            })
        self.stdout.write(self.style.SUCCESS("Seeded demo categories/products"))
