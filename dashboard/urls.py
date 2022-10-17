from django.urls import path

from .views import doctor_dashboard, patient_dashboard

urlpatterns = [
    path('D3mzy-108/', patient_dashboard, name='patient_dashboard'),
    
    path('Demzy-108/', doctor_dashboard, name='doctor_dashboard'),
]
