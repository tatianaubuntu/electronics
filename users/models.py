from django.contrib.auth.models import AbstractUser
from django.db import models

from network.models import NULLABLE


class User(AbstractUser):
    """Класс, описывающий модель пользователя"""
    username = None
    email = models.EmailField(unique=True,
                              verbose_name='почта')
    first_name = models.CharField(max_length=15,
                                  verbose_name="имя",
                                  **NULLABLE)
    last_name = models.CharField(max_length=15,
                                 verbose_name="фамилия",
                                 **NULLABLE)
    phone = models.CharField(max_length=35,
                             verbose_name="телефон",
                             **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
