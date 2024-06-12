from typing import List

from django.contrib.auth.models import AbstractBaseUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractBaseUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='Город', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: List[str] = []

    def __str__(self):
        return f"{self.email}"


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
