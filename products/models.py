from django.db import models

from network.models import NULLABLE


class Product(models.Model):
    """Класс, описывающий информацию о продукте"""
    title = models.CharField(max_length=150,
                             verbose_name='название')
    model = models.CharField(max_length=150,
                             verbose_name='модель',
                             **NULLABLE)
    release_date = models.DateTimeField(verbose_name='дата выхода',
                                        **NULLABLE)

    def __str__(self):
        return f'{self.title} {self.model}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
