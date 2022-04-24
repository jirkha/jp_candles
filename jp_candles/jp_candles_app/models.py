from django.db import models


class Product(models.Model): # všechny druhy produktů
    name = models.CharField(max_length=256) # název produktu
    type = models.CharField(max_length=128) # typ produktu (svíčka / vonný vosk / difuzér atd.)
    production_costs = models.IntegerField() # výrobní náklady
    selling_price = models.IntegerField() # prodejní cena

    def _str__(self):
        return f"NÁZEV PRODUKTU: {self.name}, DRUH ZBOŽÍ: {self.type}, VÝROBNÍ NÁKLADY: {self.production_costs}, PRODEJNÍ CENA: {self.selling_price}"


class Sale(models.Model): # typ prodejního kanálu
    name = models.CharField(max_length=256) # např. názen trhu, název obchodu kde byla svíčka prodána, eshop atd.
    type = models.CharField(max_length=128) # trh / eshop / komisní prodej / externí spolupráce
    jp_candles = models.BooleanField() # uvádí (a/n), zda se jedná o prodejní kanál pod značkou JPcandles nebo pro výrobu pod jinou značkou (externí spolupráce)
    
    def _str__(self):
        return f"PRODEJNÍ KANÁL: {self.name}, DRUH KANÁLU: {self.type}, ZNAČKA JPcandles: {self.jp_candles}"


# class Transaction(models.Model):  # transakce

