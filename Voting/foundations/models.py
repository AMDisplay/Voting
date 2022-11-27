from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinValueValidator
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _


class Foundations(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Voting(models.Model):
    name = models.CharField(max_length=20)
    foundations = models.ForeignKey(
        Foundations,
        on_delete=models.SET_NULL,
        related_name='found_voting',
        null=True,
    )

    def __str__(self) -> str:
        return self.name

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, id_card, email, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        if not id_card:
            raise ValueError('The given id_card must be set')
        email = self.normalize_email(email)
        user = self.model(id_card=id_card, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, id_card, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(id_card, email, password, **extra_fields)

    def create_superuser(self, id_card, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(id_card, email, password, **extra_fields)


    
class User(AbstractBaseUser, PermissionsMixin):
    id_card = models.IntegerField(null=False, unique=True, validators=[MinValueValidator(8)])
    email = models.EmailField(_('email address'), blank=True)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'),default=False)
    
    voting = models.ForeignKey(
        Voting,
        on_delete=models.SET_NULL,
        related_name='found_voting',
        null=True 
    )

    foundations = models.ForeignKey(
        Foundations,
        on_delete=models.SET_NULL,
        related_name='found_voters',
        null=True
    )

    object = CustomUserManager()

    USERNAME_FIELD = 'id_card'
    REQUIRED_FIELDS = ['email']


    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    # def clean(self):
    #     super().clean()
    #     self.email = self.__class_/l)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return str(self.id_card)
