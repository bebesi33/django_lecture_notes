from django.urls import path
from . import views


urlpatterns = [
    path('', views.calculator_home, name='home'),
    path('addition/', views.addition, name='addition'),
]
