from django.urls import path
from . import views

urlpatterns = [
   path('', views.dashboard, name='dashboard'),
   path('dash/', views.desh_info, name='desh_info'),



]