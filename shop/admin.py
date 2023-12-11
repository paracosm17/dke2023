from django.contrib import admin
from .models import (
    Supplier,
    ProductOrder,
    SupplierInvoice,
    Order,
    Product,
    CartProduct,
    Category,
    ProductCategory,
    Warehouse,
    Manager
)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_code', 'address', 'phone')


@admin.register(ProductOrder)
class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ('product_code', 'supplier_order_number', 'quantity')


@admin.register(SupplierInvoice)
class SupplierInvoiceAdmin(admin.ModelAdmin):
    list_display = ('supplier_order_number', 'manager_code', 'amount', 'payment_date')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('supplier_order_number', 'manager_code', 'supplier_code', 'order_date', 'status')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_code', 'name', 'availability_status', 'price')


@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'order_number', 'quantity')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_code', 'name')


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'category')


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('product', 'available_quantity', 'reserved_quantity')


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('manager_code', 'first_name', 'last_name', 'middle_name', 'phone')
