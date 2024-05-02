from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Jobs
from .serializers import JobsSerializer
from rest_framework import generics
from rest_framework import filters

from django.db.models import FilteredRelation, Q
# class JobsAPIView(generics.RetrieveAPIView):
#     # search_fields = ['name', '$description', 'level', 'major__name', 'address__city']
#     # filter_backends = [filters.SearchFilter]
#     # queryset = Jobs.objects.all()
#     serializer_class = JobsSerializer

#     def get_queryset(self):
#         name = self.request.query_params.get("name", None)
#         if not name:
#             raise Http404
#         return Jobs.objects.filter(email=self.kwargs["email"])


# Create your views here.
@api_view(['GET'])
def getData(request):
    
    keyword = request.GET.getlist('keyword')
    
    min_salary = request.GET.get('min_salary')
    max_salary = request.GET.get('max_salary')
    level= request.GET.getlist('level')
    major = request.GET.getlist('major')
    job_address = request.GET.getlist('job_address')
    
    result = None
    print(level)
    
        
    # app = Jobs.objects.annotate(
    #  jobs__job_address=FilteredRelation(
    #      "job_address",
    #      condition=Q(address__city=job_address),
    #  ),
    # ).filter(jobs__name__regex=keyword, jobs__salary__lt = max_salary, jobs__salary__gt = min_salary, jobs__level = level, job__major = major)

    app = Jobs.objects.filter(name__regex=keyword, description__regex=keyword, level = level)

    serializer = JobsSerializer(app, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postData(request):
    serializer = JobsSerializer(data=request.data)
    print(serializer)
    print(serializer.is_valid())
    # if serializer.is_valid():
        
    serializer.save()

    return Response(serializer.data)
