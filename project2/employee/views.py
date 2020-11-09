from django.views import generic
from .models import Employee

class IndexView(generic.ListView):
    model = Employee