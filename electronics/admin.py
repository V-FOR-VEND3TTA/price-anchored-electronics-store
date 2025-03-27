from django.contrib import admin
from .models import Product, FakeCompetitor

admin.site.register(Product)
admin.site.register(FakeCompetitor)
