from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Major
from .serializers import MajorSerializer


# Create your views here.
@api_view(['GET'])
def getData(request):
    app = Major.objects.all()
    serializer = MajorSerializer(app, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postData(request):
    serializer = MajorSerializer(data=request.data)

    if serializer.is_valid():
        
        serializer.save()
        
        return Response(serializer.data)
