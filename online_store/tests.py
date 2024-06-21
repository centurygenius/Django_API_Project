from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Item, Supplier

# Create your tests here.
class TestsInventory(APITestCase):
    def test_suppliercreateview(self):
        item_info = Item.objects.create(name='Item Test')
        url = reverse('supplier-list')
        data = {'name': 'Supplier Test', 'contact_info': 'test@anything.com'}
        response = self.client.post(url, data, item_info, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_itemcreateview(self):
        supplier = Supplier.objects.create(name='Supplier Test', contact_info='test@anything.com')
        url = reverse('item-list')
        data = {'name': 'Item Test', 'description': 'Description Test', 'price': '70.00', 'suppliers': [supplier.id]}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
