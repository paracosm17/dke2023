from django.contrib import admin
from .models import (
    Client,
    CustomerInvoice,
    Cart,
    Supplier,
    ProductOrder,
    SupplierInvoice,
    Order,
    Product,
    CartProduct,
    Category,
    ProductCategory,
    Warehouse,
    Manager,
    OrderSupplier
)


@admin.register(OrderSupplier)
class OrderSupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_order_number', 'manager_code', 'supplier_code', 'order_date', 'status')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_code', 'last_name', 'first_name', 'address', 'phone')


@admin.register(CustomerInvoice)
class CustomerInvoiceAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'payment_date', 'amount_due', 'status')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'promo_code', 'discount', 'status')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'manager_code', 'client', 'order_date')


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_code', 'address', 'phone')


@admin.register(ProductOrder)
class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ('product_code', 'supplier_order_number', 'quantity')


@admin.register(SupplierInvoice)
class SupplierInvoiceAdmin(admin.ModelAdmin):
    list_display = ('supplier_order_number', 'manager_code', 'amount', 'payment_date')


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
