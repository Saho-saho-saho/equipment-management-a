from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView
from django.urls import reverse_lazy
from .models import Equipment
from .forms import EquipmentForm

class IndexView(ListView):
    model = Equipment
    template_name = 'equipments/equipment_list.html'
    context_object_name = 'equipments'
    ordering = '-created_at'

class CreateView(CreateView):
    form_class = EquipmentForm
    template_name = 'equipments/create.html'
    success_url = reverse_lazy("equipments:equipment_list")

    def form_valid(self, form):
        equipment = form.save(commit=False)
        equipment.save()
        return super().form_valid(form)

class DetailView(DetailView):
    model = Equipment
    template_name = 'equipments/detail.html'