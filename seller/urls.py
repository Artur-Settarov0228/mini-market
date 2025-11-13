from django.urls import path
from .views import add_product, dashboard

urlpatterns = [
    path("add_product/", add_product, name="add_product"),
    path("dashboard", dashboard, name="dashboard" )

]
