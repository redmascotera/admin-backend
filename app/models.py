"""APP Models"""

# gascarcella: NOTE: I will probably want to split this file into multiple ones.
# starting with a single one for speed-up purposes

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class TimestampedModel(models.Model):
    """Timestamped Model"""

    created_at = models.DateTimeField(
        _("creado"),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        _("actualizado"),
        auto_now=True,
    )

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    """Custom User Manager"""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a user with the given email and password."""

        if not email:
            raise ValueError("The given email must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular user with the given email and password."""

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a superuser with the given email and password."""

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Custom User Model"""

    username = None
    email = models.EmailField(_("email"), unique=True)

    # Set the custom user manager
    objects = UserManager()
    # Set the email as the USERNAME_FIELD
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Phone(TimestampedModel):
    phone = models.CharField(
        _("telefono"),
        max_length=80,
        unique=True,
    )


class Owner(TimestampedModel):
    """Pet Owner"""

    name = models.CharField(
        _("nombre"),
        max_length=80,
        blank=True,
        default="",
    )
    email = models.EmailField(
        _("email"),
        blank=True,
        default="",
    )

    phones = models.ManyToManyField(
        Phone,
        related_name="owners",
        verbose_name=_("telefonos"),
    )


class Pet(TimestampedModel):
    """Pet Model"""

    name = models.CharField(
        _("nombre"),
        max_length=80,
    )
    owner = models.ForeignKey(
        Owner,
        related_name="pets",
        verbose_name=_("dueño"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.name


class PetTag(TimestampedModel):
    """Pet Tag Model"""

    owner = models.ForeignKey(
        Owner,
        related_name="tags",
        verbose_name=_("dueño"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
    pet = models.OneToOneField(
        Pet,
        related_name="tags",
        verbose_name=_("mascota"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
    tag = models.CharField(
        _("chapa"),
        max_length=80,
        unique=True,
    )
    code = models.CharField(
        _("codigo"),
        max_length=80,
        blank=True,
        default="",
    )
    phones = models.ManyToManyField(
        Phone,
        related_name="tags",
        verbose_name=_("telefonos"),
    )
