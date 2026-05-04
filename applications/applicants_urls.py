from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.applicant_dashboard, name='applicant_dashboard'),
    path('status/', views.application_status, name='application_status'),
]
