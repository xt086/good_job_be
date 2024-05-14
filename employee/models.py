from address.models import Address
from base.base_model import *
from base.enum import Gender, Level
from jobs.models import Jobs
from major.models import Major
from django.contrib.auth.models import AbstractBaseUser

from user_app.models import AppUser
# Create your models here.
class Employee(AbstractBaseUser):
    user = models.OneToOneField(AppUser, null=False, blank=False,
                                           on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=True)
    number = models.CharField(max_length=128, null=True)
    gender = models.CharField(
        max_length = 1,
        choices=Gender.choices,
        null=True
    )
    age = models.IntegerField(null=True,)

    REGISTRATION_CHOICES = [
        ('username', 'Username'),
        ('google', 'Google'),
    ]
    registration_method = models.CharField(
        max_length=10,
        choices=REGISTRATION_CHOICES,
        default='google'
    )
    employee_address = models.OneToOneField(Address, null=True, blank=False,
                                           on_delete=models.CASCADE)
    

    personal_introduction = models.CharField(max_length = 2000)

    level= models.CharField(
        max_length = 2,
        choices=Level.choices,
        null=True
    )

    cv = models.FileField(upload_to='cv/%Y/%m/%d')
    min_salary = models.DecimalField(max_digits=3, decimal_places=1, null=True)

    max_salary = models.DecimalField(max_digits=3, decimal_places=1, null=True)

    major = models.ManyToManyField(Major)

    prefer_jobs = models.ManyToManyField(Jobs)
