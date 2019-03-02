
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('check/', views.loan_status_check),
    path('client/', views.loan_client),
]
