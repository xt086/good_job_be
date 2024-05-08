from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse
from django.template import RequestContext
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Employee
from .serializers import EmployeeSerializer
from .upload_file.form import DocumentForm
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
    

@api_view(['VIEW', 'POST'])
def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Employee(cv = request.FILES['file'])
            newdoc.save()

            # Redirect to the document list after POST
            return 200
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Employee.objects.all()

    # Render list page with the documents and the form
    return render(request, './employee/templates/list.html', {'documents': documents, 'form': form}) 
    # return render(
    #     'list.html',
    #     {'documents': documents, 'form': form},
    #     context_instance=RequestContext(request)
    # )


