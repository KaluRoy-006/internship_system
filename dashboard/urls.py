from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('applications/', views.all_applications, name='all_applications'),
    path('applications/<int:pk>/', views.application_detail, name='application_detail'),
    path('applications/<int:pk>/approve/', views.approve_application, name='approve_application'),
    path('applications/<int:pk>/reject/', views.reject_application, name='reject_application'),
    path('applications/<int:pk>/delete/', views.delete_application, name='delete_application'),
    path('approved/', views.approved_applications, name='approved_applications'),
    path('rejected/', views.rejected_applications, name='rejected_applications'),
]