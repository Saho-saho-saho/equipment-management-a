from django.urls import path
from .views import IndexView,CreateView
from . import views
#from .views import CustomCreateView as CreateView

app_name = 'equipments'
urlpatterns = [
    # path('', IndexView.as_view(), name='equipment_list'),
    path('', views.IndexView.as_view(), name='equipment_list'),
    path('equipments/create/', CreateView.as_view(), name='create'),
]