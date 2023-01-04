from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    print_name = models.CharField(max_length=120)
    filament_type = models.CharField(max_length=10)
    material_length = models.FloatField(default=0.0)
    print_time = models.CharField(max_length=30)
    print_date = models.DateField(("Date"), auto_now_add=True)
    is_academic = models.BooleanField(default=False)
    print_cost = models.FloatField(default=0.0 ,validators=[MinValueValidator(0.0), MaxValueValidator(10_000.0)])

    def __str__(self):
        return self.print_name

    class Meta:
        ordering = ['print_date']
