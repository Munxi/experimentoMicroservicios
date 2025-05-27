from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.evento_view, name='evento_view'),

]
