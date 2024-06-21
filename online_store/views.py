from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item, Supplier
from .serializers import ItemSerializer, SupplierSerializer
from rest_framework import status

# Create your views here.
class ItemListView(APIView):
    # This lists all items.
    def get(self, request):
        items = Item.objects.all() # This returns a complex data structure
        serializer = ItemSerializer(items, many=True) # This converts the data structure to JSON
        return Response(serializer.data)

class ItemCreateView(APIView):
    # This creates an item
    def post(self, request):
        serializer = ItemSerializer(data=request.data)

        #Validation check for an already existing data
        if Item.objects.filter(**request.data).exists():
            raise serializer.ValidationError('Item already exists')

        # Checks validity of the data. If the data is valid, save it to the database
        # and return a response otherwise return an error.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemDetailView(APIView):
    # This gets, updates and deletes a specified item.
    
    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        # This gets a specified item with the primary key 'pk'.
        item = self.get_object(pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk):
        # This updates an item with the primary key 'pk'.
        item = self.get_object(pk)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # This deletes an item with the primary key 'pk'.
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SupplierCreateView(APIView):
    # This creates a supplier.
    def post(self, request):
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SupplierListView(APIView):
    # This lists all suppliers.
    def get(self, request):
        suppliers = Supplier.objects.all()
        serializer = SupplierSerializer(suppliers, many=True)
        return Response(serializer.data)
    
class SupplierUpdateView(APIView):
    # This updates a supplier.
    def get_object(self, pk):
        try:
            return Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            return Response({'error': 'Supplier not found'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        # This gets a specified supplier with the primary key 'pk'.
        supplier = self.get_object(pk)
        serializer = SupplierSerializer(supplier)
        return Response(serializer.data)

    def put(self, request, pk):
        # This updates a supplier with the primary key 'pk'.
        supplier = self.get_object(pk)
        serializer = SupplierSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)