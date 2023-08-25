from rest_framework.serializers import ModelSerializer
from .models import *
class supliersSerializer(ModelSerializer):
    class Meta:
        model = Suplier
        fields = '__all__'
class GroupsSerializer(ModelSerializer):
    class Meta:
        model=ProductsGroup
        fields = '__all__'
class CustomersSerializer(ModelSerializer):
    class Meta:
        model=ProductsGroup
        fields = '__all__'
class ShopsSerializer(ModelSerializer):
    class Meta:
        model=Shop
        fields = '__all__'
class EmployeesSerializer(ModelSerializer):
    class Meta:
        model=Employee
        fields = '__all__'
class OrdersSerializer(ModelSerializer):
    class Meta:
        model=Orders
        fields = '__all__'
class ProductsSerializer(ModelSerializer):
    class Meta:
        model=Products
        fields = '__all__'

class StorageUnitsSerializer(ModelSerializer):
    class Meta:
        model=StorageUnit
        fields = '__all__'
class StorageLinkedsSerializer(ModelSerializer):
    class Meta:
        model=StorageLinked
        fields = '__all__'
class ProductSoldsSerializer(ModelSerializer):
    class Meta:
        model=ProductSold
        fields = '__all__'
class InvoicesSerializer(ModelSerializer):
    class Meta:
        model=Invoice
        fields = '__all__'
class StoredAtsSerializer(ModelSerializer):
    class Meta:
        model=StoredAt
        fields = '__all__'

