from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import *
from .serializers import*
# Create your views here.
from .models import Major
from .serializers import MajorSerializer

from django.db.models import FilteredRelation, Q
from .service import MajorService

class APIMajor(viewsets.ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
    
    def list(self, request, *args, **kwargs):
        data = list(Major.objects.all().values())
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        keyword = request.GET.getlist('keyword')

        min_salary = request.GET.get('min_salary')
        max_salary = request.GET.get('max_salary')
        level= request.GET.getlist('level')
        major = request.GET.getlist('major')
        job_address = request.GET.getlist('job_address')
        
        result = None
        print(keyword)
        filter = None

        if(keyword):
            for word in keyword:
                filter = filter or (Q(name__regex=word) and Q(description__regex=word))

        if(level):
            filter = filter and Q(level=level)

        if(min_salary and max_salary):
            filter = filter or (Q( jobs__salary__lt=min_salary) and Q(jobs__salary__gt=min_salary))
        now = datetime.now()
        filter = filter and Q( jobs__expired_time__gt=now)
        if(filter):

            app = Major.objects.filter(filter)
        else:
            app = []
            # app = Major.objects.all()

        serializer = MajorSerializer(app, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
     
        MajorService.create(request.data)

    def destroy(self, request, *args, **kwargs):
        data = Major.objects.filter(id=kwargs['pk'])
        if data:
            data.delete()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Product delete Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Product data not found", "status": status_code})

    def update(self, request, *args, **kwargs):
        details = Major.objects.get(id=kwargs['pk'])
        serializer_data = Major(
            details, data=request.data, partial=True)
        if serializer_data.is_valid():
            serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Product Update Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Product data Not found", "status": status_code})
