
from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Company
from .serializers import CompanySerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.decorators import action

from django.db.models import FilteredRelation, Q

from django.core.serializers import serialize
class APICompany(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    serializer_address = AddressSerializer
    serializer_major = MajorSerializer

    def list(self, request, *args, **kwargs):
        data = Company.objects.all()
        # serial_datas = []
        # for data_detail in data:
        #     print(CompanySerializer(data=data_detail))
        #     serial_datas.append(CompanySerializer(data=data_detail).initial_data)

        serializer = CompanySerializer(data,many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        
        serializer_data = CompanySerializer(data=request.data)
     
        if serializer_data.is_valid():
        
            serializer_data.save()
        
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Job Added Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "please fill the datails", "status": status_code})

    def destroy(self, request, *args, **kwargs):
        data = Company.objects.filter(id=kwargs['pk'])
        if data:
            data.delete()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Product delete Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Product data not found", "status": status_code})

    def update(self, request, *args, **kwargs):
        details = Company.objects.get(id=kwargs['pk'])
        serializer_data = Company(
            details, data=request.data, partial=True)
        if serializer_data.is_valid():
            serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Product Update Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Product data Not found", "status": status_code})
        
    