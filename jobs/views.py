from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import *
from .serializers import*
# Create your views here.
from .models import Jobs
from .serializers import JobsSerializer
from rest_framework.decorators import action
from .upload_file.form import DocumentForm
from django.db.models import Q
from minio_service.minio_handler import MinioHandler
from io import BytesIO
from rest_framework.decorators import api_view
# Create your views here.

class APIJobs(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer

    def list(self, request, *args, **kwargs):
        id = request.GET.getlist('id')
        keyword = request.GET.getlist('keyword')

        min_salary = request.GET.get('min_salary')
        max_salary = request.GET.get('max_salary')
        level= request.GET.getlist('level')
        majors = request.GET.getlist('major')
        job_addresses = request.GET.getlist('job_address')
        
        filter = None
        if(id):
            filter = filter and Q(id =id) 
        if(keyword):
            for word in keyword:
                filter = filter or (Q(name__regex=word) and Q(description__regex=word))

        if(level):
            filter = filter and Q(level=level)

        if(min_salary and max_salary):
            filter = filter or (Q( jobs__salary__lt=min_salary) and Q(jobs__salary__gt=min_salary))

        if(majors):
            for major in majors:
                filter = filter and Q(major__name =major)  


        if(job_addresses):
            for address in job_addresses:
                filter = filter and Q(address__city =address) 

        now = datetime.now()
        filter = filter and Q( jobs__expired_time__gt=now)
        if(filter):

            app = Jobs.objects.filter(filter)
        else:
            # app = []
            app = Jobs.objects.all()

        serializer = JobsSerializer(app, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):

                
        serializer_data = JobsSerializer(data=request.data)
        
        if serializer_data.is_valid():
            serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Job Added Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "please fill the datails", "status": status_code})

    def destroy(self, request, *args, **kwargs):
        data = Jobs.objects.filter(id=kwargs['pk'])
        if data:
            data.delete()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Job delete Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Job data not found", "status": status_code})

    def update(self, request, *args, **kwargs):
        details = Jobs.objects.get(id=kwargs['pk'])
        serializer_data = Jobs(
            details, data=request.data, partial=True)
        if serializer_data.is_valid():
            serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Job Update Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Job data Not found", "status": status_code})
    

@api_view(['POST'])
def postFile(request):
    
        # Handle file upload
        form = DocumentForm("POST", request.data["file"])
        employee_id = request.data["employeeId"]
        job_id = request.data["jobId"]
        try:
            data = request.data['file'].read()

            file_name = str(job_id) + "/" + str(employee_id)+".pdf"

            data_file = MinioHandler().get_instance().put_object(
                file_name=file_name,
                file_data=BytesIO(data),
                content_type="pdf"
            )
            return data_file
        
        except Exception as e:
            raise e
        

@api_view(['GET'])
def getFile(request):
    
        # Handle file upload
        
        employee_id = request.GET.get["employeeId"]
        job_id = request.GET.get["jobId"]
        try:
            
            prefix = None
            if job_id:
                if employee_id:
                    prefix = job_id+"/"+employee_id+"/"
                    employee= Employee.objects.filter(id = employee_id)
                    
                    data = {
                        "employee": employee,
                        "cv_url":  "http://localhost:9000" + job_id + "/" + employee.id
                    }
                    return data
                else:
                    prefix = job_id+"/"
            minio = MinioHandler()
            endpoint_files = minio.list_obj(prefix= prefix)
            employee_ids =[]
            for endpoint_file in endpoint_files:
                employee_ids.append(str(endpoint_file).split("/")[1].split(".")[0])
            employee_data = []
            if(employee_ids != []):
                employees= Employee.objects.filter(id__in = employee_ids)
                for employee in employees:
                    data = {
                        "employee": employee,
                        "cv_url":  "http://localhost:9000" + job_id + "/" + employee.id
                    }
            return employee_data
        except Exception as e:
            raise e
            
