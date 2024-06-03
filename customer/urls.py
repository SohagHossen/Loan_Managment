from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer, name='customer'),
    path('cus/', views.customer_list, name='cus'),
    path('cus_reg/',views.customer_reg, name='customer_reg'),
    path('reg/',views.reg_cus, name='registrations'),


]