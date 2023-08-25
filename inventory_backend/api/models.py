from django.db import models
from jsonfield import JSONField



class ProductsGroup(models.Model):
    
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)+'-'+ self.name 

class Suplier(models.Model):
    name = models.CharField(max_length=50, unique=True)
    phone = models.BigIntegerField(null =False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.id)+'-'+ self.name 
class Products(models.Model):
   
    photo = models.TextField(blank=True, null=True)
    group = models.ForeignKey(
        ProductsGroup, related_name="inventories", null=True, on_delete=models.SET_NULL
    )
   
    name = models.CharField(max_length=255) 
    price = models.FloatField(default=0)
    supId=models.ForeignKey(Suplier,related_name="supliers",null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    productBeingSold = models.BooleanField(default=True)

    

    def __str__(self):
        
        return str(self.id)+'-'+ self.name 




class Shop(models.Model):

    name = models.CharField(max_length=50,unique=True)
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.id)+'-'+ self.name 

class Customer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    phone = models.BigIntegerField(null =False)
    address = models.CharField(max_length=100,null=False)
    email= models.EmailField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)+'-'+ self.name 

class Employee(models.Model):
    name = models.CharField(max_length=50, unique=True)
    phone = models.BigIntegerField(null =False)
    branchId = models.ForeignKey(Shop, on_delete=models.SET_NULL,null=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    jobStatus = models.BooleanField(default=True)
    def __str__(self):
        return str(self.id)+'-'+ self.name 
class Orders(models.Model):
    customerId = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True)
    branchId =models.ForeignKey(Shop, on_delete=models.SET_NULL,null=True)
    empId = models.ForeignKey(Employee, on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)+' at '+ str(self.branchId) + ' for '+str(self.customerId)
def random_string():
    return str(random.randint(10000, 99999))
class Invoice(models.Model):

    orderId = models.ForeignKey(Orders, on_delete=models.CASCADE)

    amount = models.BigIntegerField(null=True)
    products = JSONField(null=True)
    def __str__(self):
        return str(self.id)


class ProductSold(models.Model):
    productId = models.ForeignKey(Products, on_delete=models.PROTECT)
    orderId = models.ForeignKey(Orders, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null =False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta : 
        unique_together = (("productId","orderId"))
    def __str__(self):
        return str(self.id)



class StorageUnit(models.Model):
    unitKey=models.CharField(max_length=50,unique=True)
    capacity = models.PositiveIntegerField(null=False, default=10)
    def __str__(self):
        return str(self.id)+'-'+ self.unitKey

class StoredAt(models.Model):
    productId=models.ForeignKey(Products, on_delete=models.CASCADE)
    storageId=models.ForeignKey(StorageUnit, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(null=False, default=0)
    class Meta : 
        unique_together = (("productId","storageId"))
    def __str__(self):
        return str(self.id)


    
class StorageLinked(models.Model):
    storageId = models.ForeignKey(StorageUnit, on_delete=models.CASCADE)
    ShopId = models.ForeignKey(Shop, on_delete=models.CASCADE)
    class Meta : 
        unique_together = (("storageId","ShopId"))
    def __str__(self):
        return str(self.id)


