from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from foundations.models import Voting, Found
from users.manager import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    id_card = models.IntegerField(null=False, unique=True)
    email = models.EmailField(_('email address'), blank=True)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)

    voting = models.ForeignKey(
        Voting,
        on_delete=models.CASCADE,
        related_name='votings',
        null=True,
        blank=True
    )

    foundations = models.ForeignKey(
        Found,
        on_delete=models.CASCADE,
        related_name='found',
        null=True,
        blank=True
    )

    objects = CustomUserManager()

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

    def __str__(self):
        return str(self.id_card)
