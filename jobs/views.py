from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Jobs
from .serializers import JobsSerializer
from rest_framework import generics
from rest_framework import filters

class JobsAPIView(generics.RetrieveAPIView):
    # search_fields = ['name', '$description', 'level', 'major__name', 'address__city']
    # filter_backends = [filters.SearchFilter]
    # queryset = Jobs.objects.all()
    serializer_class = JobsSerializer

    def get_queryset(self):
        name = self.request.query_params.get("name", None)
        if not name:
            raise Http404
        return Jobs.objects.filter(email=self.kwargs["email"])


# Create your views here.
# @api_view(['GET'])
# def getData(request):
    
#     name = request.request_params.name
#     expired_time = request.request_params.expired_time
#     salary = request.request_params.salary
#     description = request.request_params.description
#     level= request.request_params.level
#     major = request.request_params.major
#     job_address = request.request_params.job_address
#     app = Jobs.objects.filter(name = name, )
#     serializer = JobsSerializer(app, many=True)
#     return Response(serializer.data)


# @api_view(['POST'])
# def postData(request):
#     serializer = JobsSerializer(data=request.data)

#     if serializer.is_valid():
        
#         serializer.save()
        
#         return Response(serializer.data)
