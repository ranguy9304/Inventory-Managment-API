from django.urls import path
from .views import *

urlpatterns = [
    path('',getRoutes,name="routes"),
    path('supliers/',getSupliers,name="products"),
    path('suplier/new/',createSuplier,name="creater suplier"),
    path('suplier/<str:pk>/',getSuplier,name="suplier"),
    path('suplier/<str:pk>/update/',updateSuplier,name="update"),
    path('suplier/<str:pk>/delete/',deleteSuplier,name="delete"),
    path('suplier/<str:pk>/gives_products/',get_products_by_supplier,name="products suplied"),
    
    ###############################
    path('groups/',getGroups,name="products"),
    path('group/new/',createGroup,name="creater Group"),
    path('group/<str:pk>/',getGroup,name="Group"),
    path('group/<str:pk>/update/',updateGroup,name="update"),
    path('group/<str:pk>/delete/',deleteGroup,name="delete"),
    path('group/most_popular/<str:duration>',getMostPopularGroup,name="most popular group"),
    ###############################################3
    path('customer/spent/<str:pk>/<str:duration>',getCustomerSpent,name="products"),
    path('customers/',getCustomers,name="products"),
    path('customer/<str:pk>/products_ordered/<str:duration>',get_orders_of_customer,name="products"),
    path('customer/new/',createCustomer,name="creater Customer"),
    path('customer/<str:pk>/',getCustomer,name="Customer"),
    path('customer/<str:pk>/update/',updateCustomer,name="update"),
    path('customer/<str:pk>/delete/',deleteCustomer,name="delete"),
    path('customers/get_fav/<str:pk>',get_fav,name="products"),
    path('customers/download_stats/',download_stats,name="products"),
    ###############################################3
    path('shops/',getShops,name="products"),
    path('shop/new/',createShop,name="creater Shop"),
    path('shop/<str:pk>/',getShop,name="Shop"),
    path('shop/<str:pk>/revenue/<str:month>',get_shop_revenue,name="Shop"),
    path('shop/<str:pk>/update/',updateShop,name="update"),
    path('shop/<str:pk>/delete/',deleteShop,name="delete"),
    path('shop/<str:pk>/storage_unit_assigned/',which_storage_unit,name="delete"),
    path('shops/most_popular/<str:duration>',get_most_popular_shop,name="most popular shop"),
    path('shop/<str:pk>/has_employees/',get_employees_by_shop,name="delete"),
    path('shop/<str:pk>/has_products/',get_products_by_shop,name="delete"),
    path('shops/total_revenue/<str:unit>',get_total_revenue,name="products"),
    path('shop/<str:pk>/avg_orders/',get_avg_orders_per_month,name="delete"),
    path('shop/<str:pk>/avg_revenue/',get_avg_revenue_per_month,name="delete"),

    ###############################################3
    path('employees/',getEmployees,name="products"),
    path('employee/new/',createEmployee,name="creater Employee"),
    path('employee/<str:pk>/',getEmployee,name="Employee"),
    path('employee/<str:pk>/update/',updateEmployee,name="update"),
    path('employee/<str:pk>/fire/',fireEmployee,name="update"),
    path('employee/<str:pk>/delete/',deleteEmployee,name="delete"),
    path('employees/most_sales/<str:duration>',get_employee_with_most_sales,name="update"),
     ###############################################3
    path('orders/',getOrders,name="products"),
    path('order/new/',createOrder,name="creater Order"),
    path('order/<str:pk>/',getOrder,name="Order"),
    path('order/<str:pk>/update/',updateOrder,name="update"),
    path('order/<str:pk>/delete/',deleteOrder,name="delete"),
    path('order/<str:pk>/has_products/',order_has_products,name="delete"),

     ###############################################3
    path('products/',getProducts,name="products"),
    path('products/filter/<str:filter>/<str:Fid>',getProductsFilter,name="products"),
    path('product/<str:pk>/customers_who_bought',get_customer_who_bought,name="products"),
    path('product/new/',createProduct,name="creater Products"),
    path('product/<str:pk>/',getProduct,name="Product"),
    path('product/<str:pk>/update/',updateProduct,name="update"),
    path('product/<str:pk>/in_stock/',get_product_quantity_in_storage_units,name="delete"),

      ###############################################3
    path('storageUnits/',getStorageUnits,name="StorageUnits"),
    path('storageUnit/new/',createStorageUnit,name="creater StorageUnit"),
    path('storageUnit/<str:pk>/',getStorageUnit,name="StorageUnit"),
    path('storageUnit/<str:pk>/update/',updateStorageUnit,name="update"),
    path('storageUnit/<str:pk>/delete/',deleteStorageUnit,name="delete"),
    path('storageUnit/<str:pk>/space_left/',get_space_left,name="delete"),
    path('storageUnit/<str:pk>/products_below/<str:threshold>',get_products_below_threshold,name="delete"),
    path('storageUnit/<str:pk>/has_products',get_products_in_storage_unit,name="unit has products"),
    path('storageUnits/most_used',most_frequent_storage_unit,name="most frequenty used"),
      ###############################################3
    path('storageLinkeds/',getStorageLinkeds,name="StorageLinkeds"),
    path('storageLinked/new/',createStorageLinked,name="creater StorageLinked"),
    path('storageLinked/<str:pk>/',getStorageLinked,name="StorageLinked"),
    path('storageLinked/<str:pk>/update/',updateStorageLinked,name="update"),
    path('storageLinked/<str:pk>/delete/',deleteStorageLinked,name="delete"),
    ###############################################3
    path('productSolds/op/<str:emp>/<str:duration>',getProductSoldOps,name="ProductSolds"),
    path('productSolds/',getProductSolds,name="P roductSolds"),
    path('productSold/new/',createProductSold,name="creater ProductSold"),
    path('productSold/<str:pk>/',getProductSold,name="ProductSold"),
    path('productSold/<str:pk>/update/',updateProductSold,name="update"),
    path('productSold/<str:pk>/delete/',deleteProductSold,name="delete"),
    ###############################################3
    path('invoices/',getInvoices,name="ProductSolds"),
    path('invoice/new/',createInvoice,name="creater Invoice"),
    path('invoice/<str:pk>/',getInvoice,name="Invoice"),
    path('invoice/<str:pk>/update/',updateInvoice,name="update"),
    path('invoice/<str:pk>/delete/',deleteInvoice,name="delete"),
    path('invoice/<str:pk>/download/',downloadInvoice,name="delete"),
    #######################################################
    path('storedAts/',getStoredAts,name="P roductSolds"),
    path('storedAt/new/',createStoredAt,name="creater StoredAt"),
    path('storedAt/<str:pk>/',getStoredAt,name="StoredAt"),
    path('storedAt/<str:pk>/update/',updateStoredAt,name="update"),
    path('storedAt/<str:pk>/delete/',deleteStoredAt,name="delete")


]