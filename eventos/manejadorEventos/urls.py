from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.evento_view, name='evento_view'),
    path('eventos/<int:ni_paciente>/', views.eventos_por_paciente, name='eventos_por_paciente')

]
