from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='store_home'),
    path('add-to-cart/<int:product_id>/', views.add_product_to_cart, name='add_to_cart'),
    path('category/<slug:category_slug>/', views.category_products, name='category_products'),
    path('product/<slug:product_slug>/', views.product_detail, name='product_detail'),
]
