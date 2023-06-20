
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _

from django.utils import timezone
from .managers import *



# Create your models here.


#Custom authentication model
class CustomNewUser(AbstractBaseUser,PermissionsMixin):
    # print("custome user")
    email = models.EmailField(_("email"),unique=True)
    username = models.CharField(_("username"), max_length=10, unique=True)
    first_name = models.CharField(_("first_name"), max_length=50, default='')
    last_name = models.CharField(_("last_name"), max_length=50, default='')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    start_date = models.DateTimeField(default=timezone.now)
 
    objects = CustomAccountManager()

    USERNAME_FIELD ='email'        #login on the admin pannel required field
    REQUIRED_FIELDS = ["username"] #super user creating field


    # for display name of a instance (object to string) on the Admin Pannel
    def __str__(self):
        return str(self.username)





        