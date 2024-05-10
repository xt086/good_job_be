from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import *
from .serializers import*
# Create your views here.
from .models import Address
from .serializers import AddressSerializer



class APIAddress(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    
    def list(self, request, *args, **kwargs):
        data = list(Address.objects.all().values())
        return Response(data)


    def destroy(self, request, *args, **kwargs):
        data = Address.objects.filter(id=kwargs['pk'])
        if data:
            data.delete()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Product delete Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Product data not found", "status": status_code})

    def update(self, request, *args, **kwargs):
        details = Address.objects.get(id=kwargs['pk'])
        serializer_data = Address(
            details, data=request.data, partial=True)
        if serializer_data.is_valid():
            serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Product Update Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Product data Not found", "status": status_code})
