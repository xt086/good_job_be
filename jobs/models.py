from address.models import Address
from base.base_model import *
from company.models import Company
from employee.models import Employee
from major.models import Major
from base.enum import  Level
from datetime import datetime    
# Create your models here.
class Jobs(Base):
    name = models.CharField(max_length=128, null=False)
    expired_time = models.DateTimeField(auto_now_add=True, blank=True)
    min_salary = models.IntegerField(null=True)
    max_salary = models.IntegerField(null=True)
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

    
    applied_jobs = models.ManyToManyField(Employee, null=True, blank=True)


