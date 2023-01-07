from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'print_name', 'material_type', 'material_length', 'print_time', 'print_date', 'is_academic', 'print_cost')


    def create(self, validated_data):
        return Student.objects.create(**validated_data)