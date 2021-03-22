from django.utils.translation import gettext_lazy as _
from django.db import models
from PIL import Image
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **other_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            email=self.normalize_email(email),
            username=username, **other_fields

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, **other_fields):

        user = self.create_user(
            email,
            password=password,
            username=username,
            **other_fields
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=60,
        unique=True,
    )
    username = models.CharField(max_length=30, unique=True)
    image = models.ImageField(verbose_name='Аватар', default='default.png', upload_to='profile_pics')

    surname = models.CharField(verbose_name='Фамилия:', max_length=150, blank=True)
    first_name = models.CharField(verbose_name='Имя:', max_length=150, blank=True)
    middle_name = models.CharField(verbose_name='Отчество:', max_length=150, blank=True)
    about = models.TextField(_('Обо мне:'), max_length=500, blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False) # a admin user; non super-user
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # a admin user; non super-user
    is_superuser = models.BooleanField(default=False) # a superuser

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ] # Email & Password are required by default.

    objects = UserManager()

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
