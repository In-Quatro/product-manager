from django.db import models


class Product(models.Model):
    """Модель Продуктов."""
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=100, verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name
