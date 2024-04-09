from django.db import models
import uuid 
# Create your models here.
class Base(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False,
         null=False) 
    
    class Meta:
        abstract=True # Set this model as Abstract


class Address(models.Model):

    street = models.CharField(max_length=300)
    district = models.CharField(max_length=300)
    city = models.CharField(max_length=200)
 
    zipcode = models.IntegerField()

    def __str__(self):
        return self.street + ' ' + self.district + ' ' + self.city

    def save(self, *args, **kwargs):
        super().save()