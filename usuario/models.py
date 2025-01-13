from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O email é obrigatório.')
        if not username:
            raise ValueError('O username é obrigatório.')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)  # Encripta a senha
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('O superusuário precisa ter is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('O superusuário precisa ter is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    ID = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150, default='')
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=150)
    matricula = models.CharField(max_length=20, unique=True, default='', blank=True)
    Usuario_TIPO = models.IntegerField(default=0)
    area_interesse = models.ManyToManyField('area_interesse.AreaInteresse')
    quantidade_orientandos = models.IntegerField(default=0)
    tema = models.CharField(max_length=150, default='', blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username