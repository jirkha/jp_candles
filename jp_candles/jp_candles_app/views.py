from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

from jp_candles_app import models

import json

# products = [{"name": "vajecny liker"}, {"name": "lilie"}]

@csrf_exempt
def list_products(request):
    if request.method == "GET":
        # safe = předchází chybám spojeným s formátem Json
        # status = zajistí, že odpověď bude mít status "ok"
        products = list(models.Product.objects.values())
        return JsonResponse(products, safe=False, status=200)
    elif request.method == "POST":
        product = request.body
        product_dict = json.loads(product)
        new_product = models.Product(**product_dict) # ** se používají místo výpisu všech sloupců vytvořených v dané tabulce
        new_product.save()
        return JsonResponse(product_dict, status=200)
    else:
        return HttpResponseNotFound("Omlouvam se, tato metoda neni dostupna")

@csrf_exempt
def product_detail(request, pk):
    try:
        product = models.Product.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return JsonResponse({"status": f"There is no product with id {pk}"}, status=404)
    
    if request.method == "GET":
        return JsonResponse(model_to_dict(product))
    elif request.method == "PUT":
        new_product_bytes = request.body
        new_product = json.loads(new_product_bytes)
        product.__dict__.update(new_product)
        product.save()
        return JsonResponse(new_product, status=201)
    elif request.method == "DELETE":
        product.delete()
        return HttpResponse(status=204)


@csrf_exempt
def list_sales(request):
    if request.method == "GET":
        # safe = předchází chybám spojeným s formátem Json
        # status = zajistí, že odpověď bude mít status "ok"
        sales = list(models.Sale.objects.values())
        return JsonResponse(sales, safe=False, status=200)
    elif request.method == "POST":
        sale = request.body
        sale_dict = json.loads(sale)
        # ** se používají místo výpisu všech sloupců vytvořených v dané tabulce
        new_sale = models.Sale(**sale_dict)
        new_sale.save()
        return JsonResponse(sale_dict, status=200)
    else:
        return HttpResponseNotFound("Omlouvam se, tato metoda neni dostupna")


@csrf_exempt
def sale_detail(request, pk):
    try:
        sale = models.Sale.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return JsonResponse({"status": f"There is no sale with id {pk}"}, status=404)

    if request.method == "GET":
        return JsonResponse(model_to_dict(sale))
    elif request.method == "PUT":
        new_sale_bytes = request.body
        new_sale = json.loads(new_sale_bytes)
        sale.__dict__.update(new_sale)
        sale.save()
        return JsonResponse(new_sale, status=201)
    elif request.method == "DELETE":
        sale.delete()
        return HttpResponse(status=204)
