from address.models import Address
from base.base_model import *
from company.models import Company
from major.models import Major
from base.enum import  Level
from datetime import datetime    
# Create your models here.
class Jobs(Base):
    name = models.CharField(max_length=128, null=False)
    expired_time = models.DateTimeField(auto_now_add=True, blank=True)
    salary = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    description = models.CharField(max_length = 2000)
    level= models.CharField(
        max_length = 2,
        choices=Level.choices,
        null=True
    )
    job_address = models.OneToOneField(Address, null=True, blank=True,
                                           on_delete=models.CASCADE)
    major = models.ManyToManyField(Major)  

    company = models.ForeignKey(Company, on_delete=models.CASCADE)


