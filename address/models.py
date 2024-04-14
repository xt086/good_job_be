from base.base_model import *
# Create your models here.
class Address(models.Model):

    street = models.CharField(max_length=300)
    district = models.CharField(max_length=300)
    city = models.CharField(max_length=200)
 
    zipcode = models.IntegerField()