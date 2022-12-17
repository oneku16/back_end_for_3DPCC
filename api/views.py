from django.shortcuts import render
from .models import Student, Client
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def new_print(request, first_name, last_name, ):

    if request.method == 'POST':
        student_first_name = request.POST('student_name')
        student_last_name = request.POST('student_name')
        student = Student(student_first_name, student_last_name)

        
