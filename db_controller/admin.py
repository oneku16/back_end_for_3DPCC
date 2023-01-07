from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_of_students = ('first_name', 'last_name', 'print_name', 'material_type', 'material_length', 'print_time', 'print_date', 'is_academic', 'print_cost')


admin.site.register(Student, StudentAdmin)


