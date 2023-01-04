from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
from .models import Student



'''
{
    "id",
    "first_name" : "Elnazar",
    "last_name" : "Ulanbek",
    "print_nmae" : "demo",
    "filament_type" : "ABS",
    "material_length": 8.51,
    "print_time" : "0-12-34",
    "print_date" : "12/12/2022",
    "is_academic" : true,
    "print_cost" : 55.2
}
'''

@api_view(['POST'])
def save_print(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        # student = Student(*request.data)
        # student.save()
        # print(request.data)
            return Response({'post': serializer.data})

