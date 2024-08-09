from django.urls import path
from .views import IndexView,CreateView,DetailView
from . import views

app_name = 'equipments'
urlpatterns = [
    # path('', IndexView.as_view(), name='equipment_list'),
    path('', views.IndexView.as_view(), name='equipment_list'),
    path('equipment_list/', views.IndexView.as_view(), name='equipment_list'),
    path('equipments/create/', CreateView.as_view(), name='create'),
    path('equipments/<int:pk>/', DetailView.as_view(), name='detail'),
]