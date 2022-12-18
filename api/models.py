from django.db import models
from datetime import datetime


class Student(models.Model):

    id = models.IntegerField(primary_key=True)
    print_date = models.DateField(max_length=10, default=datetime.now().strftime("%Y-%m-%d"))
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    print_name = models.CharField(max_length=100)
    print_cost = models.FloatField(default=50)
    print_weight = models.FloatField(default=0)
    is_academic = models.BooleanField(default=False)

    def __str__(self):
        return [self.id, self.print_date, self.first_name, 
                self.last_name, self.print_name, self.print_cost,
                self.print_weight, self.is_academic]
    class Meta:
        ordering = ['print_date', 'first_name', 'last_name']

class Client(models.Model):

    id = models.IntegerField(primary_key=True)
    print_date = models.DateField(max_length=10, default=datetime.now().strftime("%Y-%m-%d"))
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    print_name = models.CharField(max_length=100)
    print_cost = models.FloatField(default=50)
    print_weight = models.FloatField(default=0)

    def __str__(self):
        return [self.id, self.print_date, self.first_name, 
                self.last_name, self.print_name, self.print_cost,
                self.print_weight]
    class Meta:
        ordering = ['print_date', 'first_name', 'last_name']