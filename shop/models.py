from django.db import models


# Create your models here.
class Client(models.Model):
    # Код клиента (PK4)
    client_code = models.IntegerField(primary_key=True, verbose_name='Идентифицирующий код клиента')
    # Фамилия
    last_name = models.CharField(max_length=100, verbose_name='Фамилия клиента')
    # Имя
    first_name = models.CharField(max_length=100, verbose_name='Имя клиента')
    # Адрес
    address = models.CharField(max_length=255, verbose_name='Адрес клиента')
    # Телефон
    phone_number = models.BigIntegerField(verbose_name='Номер мобильного телефона клиента')

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.client_code})"


class Order(models.Model):
    # Номер заказа клиента (PK)
    order_number = models.IntegerField(primary_key=True, verbose_name='Идентифицирующий номер заказа клиента')

    # Код менеджера
    manager_code = models.IntegerField(verbose_name='Идентифицирующий код менеджера, который обрабатывает заказ клиента')

    # Код клиента
    client_code = models.IntegerField(verbose_name='Идентифицирующий код клиента, который совершил заказ')

    # Дата оформления
    order_date = models.DateTimeField(verbose_name='Дата оформления заказа')

    def __str__(self):
        return f"Order #{self.order_number} by Client {self.client_code}"


