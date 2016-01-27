# Django custom model as inspired from:
#   https://docs.djangoproject.com/en/1.8/topics/auth/customizing/#a-full-example
#   https://github.com/jcugat/django-custom-user/blob/master/custom_user/models.py

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils.translation import ugettext as _
from timezone_field import TimeZoneField
from django.utils import timezone as tz

class AhaUserManager(BaseUserManager):
    def create_user(self, email, gender, password=None):
        """
        Creates and saves a User with the given email, gender and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            gender=gender,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, gender, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
                                password=password,
                                gender=gender
                                )
        user.is_admin = True
        user.save(using=self._db)
        return user


class AhaUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name=_('email address'),
        max_length=255,
        unique=True,
        db_index=True
    )
    GENDERS = (
        ("m", _("male")),
        ("f", _("female")),
        ("x", _("unknown"))
    )
    gender = models.CharField(choices=GENDERS, default="x", max_length=1, verbose_name=_("gender"))

    how_to_call = models.CharField(max_length=101, blank=True, verbose_name=_("How to call you"))

    timezone = TimeZoneField(default="Europe/Prague", verbose_name=_("Timezone"))

    remind_hour = models.IntegerField(choices=[(i, i) for i in range(1,25)], default=20, verbose_name=_("reminder hour"))

    is_admin = models.BooleanField(_('Admin'),default=False, help_text=_(
            'Designates whether the user can log into this admin site.'))

    is_active = models.BooleanField(_('Active'), default=True, help_text=_(
        'Designates whether this user should be treated as '
        'active. Unselect this instead of deleting accounts.'))

    date_joined = models.DateTimeField(_('date joined'), default=tz.now)

    objects = AhaUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['gender']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

# signal attached to the social auth
from django.dispatch import receiver
from allauth.account.signals import user_signed_up

@receiver(user_signed_up)
def set_gender(sender, **kwargs):

    # get the gender info from google
    user = kwargs.pop('user')
    extra_data = user.socialaccount_set.filter(provider='google')[0].extra_data
    gender = extra_data['gender']

    print("User signed up:", user)

    if gender == 'male':
        user.gender = "m"
    elif gender == "female":
        user.gender = 'f'
    else:
        # because the default is unknown.
        user.gender = "x"

    user.save()