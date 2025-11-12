from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('category/<int:category_id>/<slug:category_slug>/', views.category_products, name='category_products'),
    path('cart/add/<int:product_id>/', views.add_product_to_cart, name='add_product_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_cart_item, name='remove_cart_item'),
]
