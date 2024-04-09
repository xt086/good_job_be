from base.base_model import *
from base.enum import Gender, Level
from jobs.models import Jobs
from major.models import Major
# Create your models here.
class Employee(Base):
    name = models.CharField(max_length=128, null=False)
    number = models.CharField(max_length=128, null=False)
    gender = models.CharField(
        max_length = 1,
        choices=Gender.choices,
        null=False
    )
    age = models.IntegerField(null=False,)
    email = models.EmailField(max_length=254,null=False,)
    employee_address = models.OneToOneField(Address, null=False, blank=False,
                                           on_delete=models.CASCADE, related_name='employee_address')
    

    personal_introduction = models.CharField(max_length = 2000)

    level= models.CharField(
        max_length = 2,
        choices=Level.choices,
        null=False
    )

    min_salary = models.DecimalField(max_digits=3, decimal_places=1, null=False)

    max_salary = models.DecimalField(max_digits=3, decimal_places=1, null=False)

    major = models.ManyToManyField(Major)

    prefer_jobs = models.ManyToManyField(Jobs)
