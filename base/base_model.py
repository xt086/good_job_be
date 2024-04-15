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

