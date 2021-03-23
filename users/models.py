from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **other_fields):
        user = self.model(
            email=self.normalize_email(email),
            username=username, **other_fields

        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True,)
    username = models.CharField(max_length=30, unique=True)
    image = models.ImageField(verbose_name='Аватар', default='default.png', upload_to='profile_pics')
    name = models.CharField(verbose_name='Имя:', max_length=150, blank=True)
    surname = models.CharField(verbose_name='Фамилия:', max_length=150, blank=True)
    middle_name = models.CharField(verbose_name='Отчество:', max_length=150, blank=True)
    about = models.TextField(verbose_name='Обо мне:', max_length=500, blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
