from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator,RegexValidator
from django.core.exceptions import ValidationError

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'),unique=True)
    phone_regex=RegexValidator(regex=r'^[6-9]\d{9}$', message="Must be Valid Phone number , should not include country Code & must have 10 digit ")
    mobile = models.CharField(validators=[phone_regex],max_length=10)
    password2 = models.CharField(max_length=40,null=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile','first_name','last_name']
    objects = UserManager()
