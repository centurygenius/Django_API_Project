from django.urls import path
from .views import ItemListView, ItemDetailView, ItemCreateView, SupplierListView, SupplierCreateView, SupplierUpdateView

urlpatterns = [
    path('items/', ItemListView.as_view()),
    path('items/create/', ItemCreateView.as_view()),
    path('items/<int:pk>/', ItemDetailView.as_view()),
    path('suppliers/create/', SupplierCreateView.as_view()),
    path('suppliers/', SupplierListView.as_view()),
    path('suppliers/<int:pk>/', SupplierUpdateView.as_view()),
    
]
