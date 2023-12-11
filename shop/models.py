from django.db import models


class Client(models.Model):
    client_code = models.IntegerField(primary_key=True, verbose_name='Код клиента')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    phone = models.IntegerField(verbose_name='Телефон')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Order(models.Model):
    order_number = models.IntegerField(primary_key=True, verbose_name='Номер заказа клиента')
    manager_code = models.IntegerField(verbose_name='Код менеджера')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Код клиента')
    order_date = models.DateTimeField(verbose_name='Дата оформления')

    def __str__(self):
        return f'Order {self.order_number}'


class CustomerInvoice(models.Model):
    order_number = models.IntegerField(primary_key=True, verbose_name='Номер заказа клиента')
    payment_date = models.DateTimeField(verbose_name='Дата оплаты')
    amount_due = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма к оплате')
    status = models.CharField(max_length=255, verbose_name='Статус')

    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Номер заказа клиента')

    def __str__(self):
        return f'Invoice for Order {self.order_number}'


class Cart(models.Model):
    order_number = models.IntegerField(primary_key=True, verbose_name='Номер заказа клиента')
    promo_code = models.CharField(max_length=255, verbose_name='Промокод')
    discount = models.IntegerField(verbose_name='Скидка')
    status = models.CharField(max_length=255, verbose_name='Статус')

    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Номер заказа клиента')

    def __str__(self):
        return f'Cart for Order {self.order_number}'


class Product(models.Model):
    product_code = models.IntegerField(primary_key=True, verbose_name='Артикул товара')
    name = models.CharField(max_length=255, verbose_name='Название товара')
    availability_status = models.BooleanField(verbose_name='Статус наличия')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.name


class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Артикул товара')
    order_number = models.IntegerField(verbose_name='Номер заказа клиента')
    quantity = models.IntegerField(verbose_name='Количество товара в заказе')

    class Meta:
        unique_together = ('product', 'order_number')

    def __str__(self):
        return f'{self.product.name} - Order {self.order_number}'


class Category(models.Model):
    category_code = models.IntegerField(primary_key=True, verbose_name='Код категории')
    name = models.CharField(max_length=255, verbose_name='Название категории товаров')

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Артикул товара')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Код категории')

    class Meta:
        unique_together = ('product', 'category')

    def __str__(self):
        return f'{self.product.name} - {self.category.name}'


class Warehouse(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Артикул товара')
    available_quantity = models.IntegerField(verbose_name='Свободное количество товара')
    reserved_quantity = models.IntegerField(verbose_name='Количество товара в резерве')

    def __str__(self):
        return f'{self.product.name} - Warehouse'


class Manager(models.Model):
    manager_code = models.IntegerField(primary_key=True, verbose_name='Код менеджера')
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=255, verbose_name='Отчество')
    phone = models.IntegerField(verbose_name='Номер телефона')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Supplier(models.Model):
    supplier_code = models.IntegerField(primary_key=True, verbose_name='Код поставщика')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    phone = models.IntegerField(verbose_name='Номер телефона для связи')

    def __str__(self):
        return f'Supplier {self.supplier_code}'


class ProductOrder(models.Model):
    product_code = models.IntegerField(verbose_name='Артикул товара')
    supplier_order_number = models.IntegerField(verbose_name='Номер заказа поставщика')
    quantity = models.IntegerField(verbose_name='Количество товара для поставки')

    class Meta:
        unique_together = ('product_code', 'supplier_order_number')

    def __str__(self):
        return f'Product {self.product_code} - Supplier Order {self.supplier_order_number}'


class SupplierInvoice(models.Model):
    supplier_order_number = models.IntegerField(primary_key=True, verbose_name='Номер заказа поставщика')
    manager_code = models.IntegerField(verbose_name='Код менеджера')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма заказа')
    payment_date = models.DateTimeField(verbose_name='Дата оплаты заказа на поставку')

    def __str__(self):
        return f'Supplier Invoice {self.supplier_order_number}'


class OrderSupplier(models.Model):
    supplier_order_number = models.IntegerField(primary_key=True, verbose_name='Номер заказа поставщика')
    manager_code = models.IntegerField(verbose_name='Идентифицирующий код менеджера')
    supplier_code = models.IntegerField(verbose_name='Идентифицирующий код поставщика')
    order_date = models.DateTimeField(verbose_name='Дата заказа')
    status = models.CharField(max_length=255, verbose_name='Статус заказа')

    def __str__(self):
        return f'Order to Supplier {self.supplier_order_number}'
