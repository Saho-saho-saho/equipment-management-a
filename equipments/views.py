from django.shortcuts import render
from django.views.generic import ListView,CreateView
from .models import Equipment
from .forms import EquipmentForm

class IndexView(ListView):
    model = Equipment
    template_name = 'equipments/equipment_list.html'
    context_object_name = 'equipments'

class CreateView(CreateView):
    form_class = EquipmentForm
    template_name = 'equipments/create.html'