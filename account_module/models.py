from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


class User(AbstractUser):
    mobile_number = models.CharField(max_length=20, verbose_name='تلفن همراه', null=True)
    avatar = models.CharField(max_length=20, verbose_name='تصویر آواتار', null=True, blank=True)
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی ایمیل')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name and self.last_name:
            return self.get_full_name()
        else:
            return self.email
