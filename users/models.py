from django.contrib.auth.models import AbstractUser
from django.db import models


class Location(models.Model):
    name = models.CharField(
        verbose_name="Локация",
        max_length=100
    )
    lat = models.DecimalField(
        verbose_name="Широта",
        max_digits=8,
        decimal_places=6
    )
    lng = models.DecimalField(
        verbose_name="Долгота",
        max_digits=8,
        decimal_places=6
    )

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class UserRoles:
    USER = 'member'
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    choices = (
        (USER, 'Пользователь'),
        (ADMIN, 'Админ'),
        (MODERATOR, 'Модератор')
    )


class User(AbstractUser):
    first_name = models.CharField(
        verbose_name="Имя",
        help_text="Введите имя пользователя до 30 знаков",
        max_length=60,
        blank=True
    )
    last_name = models.CharField(
        verbose_name="Фамилия",
        help_text="Введите фамилию пользователя до 50 знаков",
        max_length=80,
        blank=True
    )
    username = models.CharField(
        verbose_name="Логин",
        max_length=150,
        unique=True,
        help_text="Не более 150 символов, только буквы, цифры и @/./+/-/_ @/./+/-/_.",
    )
    password = models.CharField(
        verbose_name="Пароль",
        help_text="Не менее 8 символов",
        max_length=128
    )
    role = models.CharField(
        choices=UserRoles.choices,
        default='member',
        max_length=12
    )
    age = models.PositiveSmallIntegerField(
        verbose_name="Возраст",
        null=True
    )
    location = models.ManyToManyField(Location)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"Уважаемый(ая) {self.first_name} {self.last_name}!"
