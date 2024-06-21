from django.db import models

# Create your models here.
class Supplier(models.Model):
    # Supplier model inherits from the Model class.
    name = models.CharField(max_length=255)
    contact_info = models.TextField()
    items_info = models.ManyToManyField('Item', related_name='suppliers_info')
    def __str__(self):
        # Returns the name of the supplier.
        return self.name
    
class Item(models.Model):
    # Item model inherits from the Model class.
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateField(auto_now_add=True)
    suppliers = models.ManyToManyField(Supplier, related_name='items')

    def __str__(self):
        # Returns the name of the item.
        return self.name