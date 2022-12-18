from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student, Client
from .serializers import StudentSerializer


'''
{
"print_date" : "2022-12-18",
"first_name" : "Elnazar",
"last_name": "Ulanbek uulu",
"print_name": "demo",
"print_cost": 50.4,
"print_weight": 43.1,
"is_academic": true 
}
'''
@api_view(['POST'])
def new_print(request):

    if request.method == 'POST':
        
        
        print_date = request.data['print_date']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        print_name = request.data['print_name']
        print_cost = request.data['print_cost']
        print_weight = request.data['print_weight']
        is_academic = request.data['is_academic']

        student = Student(print_date=print_date, first_name=first_name, 
                          last_name=last_name, print_name=print_name, 
                          print_cost=print_cost, print_weight=print_weight, 
                          is_academic=is_academic)
        student.save()
        print(f'{print_date=}\n{first_name}\n{last_name}\n{print_name}\n{print_cost}\n{print_weight}\n{is_academic}')
        

        return HttpResponse("<h1>done<h1>")
         
