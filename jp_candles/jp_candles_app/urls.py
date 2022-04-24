from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("sales", views.SaleViewset)
router.register("products", views.ProductViewset)
router.register("transactions", views.TransactionViewset)

urlpatterns = [
    # path('products', views.list_products, name="products"),
    # path('products/<int:pk>', views.product_detail, name="product_detail"),
    # path('sales', views.list_sales, name="sales"),
    # path('sales/<int:pk>', views.sale_detail, name="sale_detail"),
    path("", include(router.urls)),
]
