from django.contrib import admin

# Register your models here.
from .models import Products,ProductsGroup,Suplier,Shop,Customer,Employee,Orders,Invoice,ProductSold,StorageUnit,StoredAt,StorageLinked


admin.site.register(Products)
admin.site.register(ProductsGroup)
admin.site.register(Suplier)
admin.site.register(Shop)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Orders)
admin.site.register(Invoice)
admin.site.register(ProductSold)
admin.site.register(StorageUnit)
admin.site.register(StoredAt)
admin.site.register(StorageLinked)
# admin.site.register(InvoiceItem)
