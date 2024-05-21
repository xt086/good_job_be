
from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Employee
from .serializers import EmployeeSerializer
from .upload_file.form import DocumentForm
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.decorators import action

from django.db.models import FilteredRelation, Q


class APIEmployee(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def list(self, request, *args, **kwargs):
        data = list(Employee.objects.all())
        return Response(data)

    def create(self, request, *args, **kwargs):

        serializer_data = EmployeeSerializer(data=request.data)

        if serializer_data.is_valid():
            serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Job Added Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "please fill the datails", "status": status_code})

    def destroy(self, request, *args, **kwargs):
        data = Employee.objects.filter(id=kwargs['pk'])
        if data:
            data.delete()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Product delete Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Product data not found", "status": status_code})

    def update(self, request, *args, **kwargs):
        details = Employee.objects.get(id=kwargs['pk'])
        serializer_data = Employee(
            details, data=request.data, partial=True)
        if serializer_data.is_valid():
            serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Product Update Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Product data Not found", "status": status_code})
        
    @action(detail=True, methods=["post"], name="upload-cv")
    def upload_cv(request, *args, **kwargs):
        # Handle file upload
        if request.method == 'POST':
            form = DocumentForm(request.POST, request.FILES)

            if form.is_valid():
                details = Employee.objects.get(id=kwargs['pk'])
                details.cv = request.FILES['file']
                details.save()

                status_code = status.HTTP_201_CREATED
                return Response({"message": "Job Added Sucessfully", "status": status_code})
            
        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return Response({"message": "Methods not support", "status": status_code}) 
