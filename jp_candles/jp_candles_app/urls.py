from django.urls import path
from . import views

urlpatterns = [
    path('products', views.list_products, name="products"),
    path('products/<int:pk>', views.product_detail, name="product_detail"),
    path('sales', views.list_sales, name="sales"),
    path('sales/<int:pk>', views.sale_detail, name="sale_detail")
]
