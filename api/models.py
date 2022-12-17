from django.db import models
from datetime import datetime


class Student(models.Model):

    print_date = models.DateField(default=datetime.now().strftime("%Y-%m-%d"))
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    print_name = models.CharField(max_length=100)
    print_cost = models.FloatField(default=50)
    print_weight = models.FloatField(default=0)
    is_academic = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['print_date']

class Client(models.Model):

    print_date = models.DateField(default=datetime.now().strftime("%Y-%m-%d"))
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    print_name = models.CharField(max_length=100)
    print_cost = models.FloatField(default=50)
    print_weight = models.FloatField(default=0)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['print_date']