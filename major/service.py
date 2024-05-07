from major.serializers import MajorSerializer
from rest_framework.response import Response
from rest_framework import status
class MajorService:
    def create(data):
        serializer_data = MajorSerializer(data=data)
        if serializer_data.is_valid():
            serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Product Added Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "please fill the datails", "status": status_code})