from django.urls import path
from .views import save_print

urlpatterns = [ path('new_print/', save_print)] 