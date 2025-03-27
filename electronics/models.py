from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    actual_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class FakeCompetitor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="competitors")
    name = models.CharField(max_length=255)
    fake_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.fake_price}"
