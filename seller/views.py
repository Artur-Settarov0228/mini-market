from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Products

def add_product(request: HttpRequest) -> HttpResponse:
    success = False
    if request.method == "POST":
        name = request.POST.get("name")
        category = request.POST.get("category")
        description = request.POST.get("description")
        price = float(request.POST.get("price") or 0)
        discount = float(request.POST.get("discount") or 0)
        rating = float(request.POST.get("rating") or 0)
        image = request.FILES.get("image")

        Products.objects.create(
            name=name,
            category=category,
            description=description,
            price=price,
            discount=discount,
            rating=rating,
            image=image
        )
        success = True

    return render(request, "add_product.html", {"success": success})

def dashboard(request:HttpRequest)->HttpResponse:
    return render(request=request, template_name="seller_dashboard.html")
