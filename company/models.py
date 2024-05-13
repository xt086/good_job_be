
from address.models import Address
from base.base_model import *

from major.models import Major
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Company(Base):
    username = models.CharField(max_length=128, null=True)
    password = models.CharField(max_length=128, null=True)
    name = models.CharField(max_length=128, null=False)
    
    age = models.IntegerField(null=False,)
    email = models.EmailField(max_length=254,null=False,)
    company_address = models.OneToOneField(Address, null=False, blank=False,
                                           on_delete=models.CASCADE)
    

    personal_introduction = models.CharField(max_length = 2000)
    major = models.ManyToManyField(Major)
    



    


