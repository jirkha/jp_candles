from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=128)
    production_costs = models.IntegerField()
    selling_price = models.IntegerField()

    def _str__(self):
        return f"NÁZEV PRODUKTU: {self.name}, DRUH ZBOŽÍ: {self.type}, VÝROBNÍ NÁKLADY: {self.production_costs}, PRODEJNÍ CENA: {self.selling_price}"
