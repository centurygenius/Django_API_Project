from django.contrib import admin
from .models import Supplier
from .models import Item

# Register your models here to show them in the admin.
admin.site.register(Item)
admin.site.register(Supplier)