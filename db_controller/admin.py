from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_of_students = [field.name for field in Student._meta.fields if field.name != "id"]


admin.site.register(Student, StudentAdmin)


