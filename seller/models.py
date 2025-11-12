from django.db import models

class Products(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Oziq-ovqat'),
        ('drinks', 'Ichimliklar'),
        ('clothes', 'Kiyim-kechak'),
        ('electronics', 'Elektronika'),
        ('appliances', 'Maishiy texnika'),
        ('accessories', 'Aksessuarlar'),
        ('kids', 'Bolalar uchun mahsulotlar'),
    ]

    name = models.CharField(max_length=128)
    description = models.TextField()
    rating = models.FloatField(default=0)
    viewers = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    discount = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.price} so'm"
