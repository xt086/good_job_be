from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Company
from .serializers import CompanySerializer


# Create your views here.
@api_view(['GET'])
def getData(request):
    app = Company.objects.all()
    serializer = CompanySerializer(app, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postData(request):
    serializer = CompanySerializer(data=request.data)

    if serializer.is_valid():
        
        serializer.save()
        
        return Response(serializer.data)
