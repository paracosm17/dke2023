# Generated by Django 5.0 on 2023-12-11 08:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_code', models.IntegerField(primary_key=True, serialize=False, verbose_name='Код категории')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории товаров')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_code', models.IntegerField(primary_key=True, serialize=False, verbose_name='Код клиента')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('phone', models.IntegerField(verbose_name='Телефон')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('manager_code', models.IntegerField(primary_key=True, serialize=False, verbose_name='Код менеджера')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('middle_name', models.CharField(max_length=255, verbose_name='Отчество')),
                ('phone', models.IntegerField(verbose_name='Номер телефона')),
            ],
        ),
        migrations.CreateModel(
            name='OrderSupplier',
            fields=[
                ('supplier_order_number', models.IntegerField(primary_key=True, serialize=False, verbose_name='Номер заказа поставщика')),
                ('manager_code', models.IntegerField(verbose_name='Идентифицирующий код менеджера')),
                ('supplier_code', models.IntegerField(verbose_name='Идентифицирующий код поставщика')),
                ('order_date', models.DateTimeField(verbose_name='Дата заказа')),
                ('status', models.CharField(max_length=255, verbose_name='Статус заказа')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_code', models.IntegerField(primary_key=True, serialize=False, verbose_name='Артикул товара')),
                ('name', models.CharField(max_length=255, verbose_name='Название товара')),
                ('availability_status', models.BooleanField(verbose_name='Статус наличия')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_code', models.IntegerField(primary_key=True, serialize=False, verbose_name='Код поставщика')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('phone', models.IntegerField(verbose_name='Номер телефона для связи')),
            ],
        ),
        migrations.CreateModel(
            name='SupplierInvoice',
            fields=[
                ('supplier_order_number', models.IntegerField(primary_key=True, serialize=False, verbose_name='Номер заказа поставщика')),
                ('manager_code', models.IntegerField(verbose_name='Код менеджера')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма заказа')),
                ('payment_date', models.DateTimeField(verbose_name='Дата оплаты заказа на поставку')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_number', models.IntegerField(primary_key=True, serialize=False, verbose_name='Номер заказа клиента')),
                ('manager_code', models.IntegerField(verbose_name='Код менеджера')),
                ('order_date', models.DateTimeField(verbose_name='Дата оформления')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.client', verbose_name='Код клиента')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerInvoice',
            fields=[
                ('order_number', models.IntegerField(primary_key=True, serialize=False, verbose_name='Номер заказа клиента')),
                ('payment_date', models.DateTimeField(verbose_name='Дата оплаты')),
                ('amount_due', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма к оплате')),
                ('status', models.CharField(max_length=255, verbose_name='Статус')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.order', verbose_name='Номер заказа клиента')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('order_number', models.IntegerField(primary_key=True, serialize=False, verbose_name='Номер заказа клиента')),
                ('promo_code', models.CharField(max_length=255, verbose_name='Промокод')),
                ('discount', models.IntegerField(verbose_name='Скидка')),
                ('status', models.CharField(max_length=255, verbose_name='Статус')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.order', verbose_name='Номер заказа клиента')),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.IntegerField(verbose_name='Артикул товара')),
                ('supplier_order_number', models.IntegerField(verbose_name='Номер заказа поставщика')),
                ('quantity', models.IntegerField(verbose_name='Количество товара для поставки')),
            ],
            options={
                'unique_together': {('product_code', 'supplier_order_number')},
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_quantity', models.IntegerField(verbose_name='Свободное количество товара')),
                ('reserved_quantity', models.IntegerField(verbose_name='Количество товара в резерве')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='Артикул товара')),
            ],
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField(verbose_name='Номер заказа клиента')),
                ('quantity', models.IntegerField(verbose_name='Количество товара в заказе')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='Артикул товара')),
            ],
            options={
                'unique_together': {('product', 'order_number')},
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Код категории')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='Артикул товара')),
            ],
            options={
                'unique_together': {('product', 'category')},
            },
        ),
    ]
