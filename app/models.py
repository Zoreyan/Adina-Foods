from django.db import models

class Product(models.Model):
    image = models.ImageField(upload_to='articles/', verbose_name='Избражение')
    title = models.CharField(max_length=30, verbose_name='Название')
    price = models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Цена')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Order(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта')
    phone = models.CharField(max_length=10, verbose_name='Номер')
    address = models.CharField(max_length=100, verbose_name='Адресс')
    text = models.TextField(max_length=400, verbose_name='Текст')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'