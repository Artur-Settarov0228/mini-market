from django.contrib import admin

# Register your models here.

from .models import Category, Product, Order, Customer, Cart, CartItem, OrderItem
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(OrderItem)