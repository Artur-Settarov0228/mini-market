from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Customer, Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', {'products': products, 'categories': categories})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

def category_products(request, category_id, category_slug):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    return render(request, 'category_products.html', {'category': category, 'products': products})

@login_required
def add_product_to_cart(request: HttpRequest, product_id: int) -> HttpResponse:
    customer, created = Customer.objects.get_or_create(user=request.user)
    cart, created = Cart.objects.get_or_create(customer=customer)
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart') 

@login_required
def remove_cart_item(request: HttpRequest, item_id: int) -> HttpResponse:
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart_view')
    
    
    

