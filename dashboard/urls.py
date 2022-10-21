from django.urls import path

from .views import doctor_dashboard, patient_dashboard

urlpatterns = [
    path('<str:username>/', patient_dashboard, name='patient_dashboard'),
    
    path('doctor/<str:username>/', doctor_dashboard, name='doctor_dashboard'),
]
