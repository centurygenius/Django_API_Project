from rest_framework import serializers
from .models import Supplier, Item

# Creates the  serializer for the Supplier model.
class SupplierSerializer(serializers.ModelSerializer):

    # Specifies the Supplier model and fields.
    class Meta:
        model = Supplier
        fields = '__all__'


# Creates the  serializer for the Item model.
class ItemSerializer(serializers.ModelSerializer):
    suppliers = SupplierSerializer(many=True, read_only=True)

    # Specifies the Item model and fields.
    class Meta:
        model = Item
        fields = '__all__'
