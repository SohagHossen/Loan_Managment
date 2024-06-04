
from django.urls import path
from . import views

urlpatterns = [
    path('', views.invoice, name='invoice'),
    path('class_data/', views.class_data.as_view()),
]