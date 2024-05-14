
from address.models import Address
from base.base_model import *

from major.models import Major
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from user_app.models import AppUser
# Create your models here.
class Company(Base):
    user = models.OneToOneField(AppUser, null=False, blank=False,
                                           on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=False)
    
    age = models.IntegerField(null=False,)
 
    company_address = models.OneToOneField(Address, null=False, blank=False,
                                           on_delete=models.CASCADE)
    

    personal_introduction = models.CharField(max_length = 2000)
    major = models.ManyToManyField(Major)
    



    

