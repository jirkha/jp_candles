from django.db import models


class Product(models.Model): # všechny druhy produktů
    name = models.CharField(max_length=256) # název produktu
    type = models.CharField(max_length=128) # typ produktu (svíčka / vonný vosk / difuzér atd.)
    production_costs = models.IntegerField() # výrobní náklady
    selling_price = models.IntegerField() # prodejní cena
    created = models.DateTimeField(auto_now_add=True) # automaticky doplní čas přidání produktu

    class Meta:
        ordering = ["created"]

    def __str__(self):
        # return f"NÁZEV PRODUKTU: {self.name}, DRUH ZBOŽÍ: {self.type}"
        return f"{self.name} (type: {self.type})"


class Sale(models.Model): # typ prodejního kanálu
    name = models.CharField(max_length=256) # např. názen trhu, název obchodu kde byla svíčka prodána, eshop atd.
    type = models.CharField(max_length=128) # trh / eshop / komisní prodej / externí spolupráce
    jp_candles = models.BooleanField() # uvádí (a/n), zda se jedná o prodejní kanál pod značkou JPcandles nebo pro výrobu pod jinou značkou (externí spolupráce)
    
    def __str__(self):
        # return f"PRODEJNÍ KANÁL: {self.name}, DRUH KANÁLU: {self.type}"
        return f"{self.name}"


class Transaction(models.Model):  # transakce
    day_of_sale = models.DateField() # datum transakce
    # prodejní kanál
    sales_channel = models.ForeignKey(Sale, related_name="sales", on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, related_name="products", on_delete=models.RESTRICT) # prodaný produkt
    quantity_of_product = models.IntegerField() # množství prodaného produktu
    # automaticky doplní čas přidání transakce
    created = models.DateTimeField(auto_now_add=True)

