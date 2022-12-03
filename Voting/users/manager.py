from django.contrib.auth.models import BaseUserManager


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
