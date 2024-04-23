from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Employee
from .serializers import EmployeeSerializer


# Create your views here.
@api_view(['GET'])
def getData(request):
    app = Employee.objects.all()
    serializer = EmployeeSerializer(app, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postData(request):
    serializer = EmployeeSerializer(data=request.data)

    if serializer.is_valid():
        
        serializer.save()
        
        return Response(serializer.data)
    




