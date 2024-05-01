from address.models import Address
from base.base_model import *
from major.models import Major
from base.enum import  Level
# Create your models here.
class Jobs(models.Model):
    name = models.CharField(max_length=128, null=False)
    expired_time = models.DateTimeField(null= False)
    salary = models.DecimalField(max_digits=3, decimal_places=1, null=False)
    description = models.CharField(max_length = 2000)
    level= models.CharField(
        max_length = 2,
        choices=Level.choices,
        null=False
    )
    job_address = models.OneToOneField(Address, null=False, blank=False,
                                           on_delete=models.CASCADE)
    major = models.ManyToManyField(Major)  


