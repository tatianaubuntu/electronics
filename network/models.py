from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

NULLABLE = {'null': True, 'blank': True}

title_tuple = (
    ('factory', 'завод'),
    ('network', 'розничная сеть'),
    ('IP', 'ИП'),
)


class Contacts(models.Model):
    """Класс, описывающий контакты звеньев сети"""
    email = models.EmailField(unique=True,
                              verbose_name='почта',
                              **NULLABLE)
    country = models.CharField(max_length=150,
                               verbose_name='страна',
                               **NULLABLE)
    city = models.CharField(max_length=150,
                            verbose_name='город',
                            **NULLABLE)
    street = models.CharField(max_length=150,
                              verbose_name='улица',
                              **NULLABLE)
    home = models.CharField(max_length=25,
                            verbose_name='дом',
                            **NULLABLE)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'контакты'
        verbose_name_plural = 'контакты'


class Network(MPTTModel):
    """Класс, описывающий информацию о сети"""
    title = models.CharField(max_length=150,
                             verbose_name='название звена сети',
                             choices=title_tuple)
    contacts = models.OneToOneField(Contacts,
                                    on_delete=models.CASCADE,
                                    verbose_name='контакты',
                                    **NULLABLE)
    products = models.ManyToManyField('products.Product',
                                      verbose_name='продукты',
                                      **NULLABLE)
    supplier = TreeForeignKey('self',
                              on_delete=models.CASCADE,
                              verbose_name='поставщик',
                              **NULLABLE,
                              related_name='children')
    arrears = models.DecimalField(max_digits=50,
                                  decimal_places=2,
                                  verbose_name='задолженность',
                                  **NULLABLE)
    creation_time = models.TimeField(auto_now_add=True,
                                     verbose_name='время создания',
                                     **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class MPTTMeta:
        parent_attr = 'supplier'
        order_insertion_by = ['title']

    class Meta:
        verbose_name = 'сеть'
        verbose_name_plural = 'сеть'
