from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'store/home.html', {'products': products, 'categories': categories})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id,)
    return render(request, 'store/product_detail.html', {'product': product})

def category_products(request, category_id, category_slug):
    category = get_object_or_404(Category, id = category_id)
    products = category.products.all()
    return render(request, 'store/category_products.html', {'category': category, 'products': products})

def add_product_to_cart(request: HttpRequest, product_id: int) -> HttpResponse:
    # Logic to add the product to the cart would go here
    return HttpResponse(f"Product {product_id} added to cart.")

