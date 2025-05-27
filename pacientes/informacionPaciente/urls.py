from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.paciente_view, name='paciente_view'),

]
