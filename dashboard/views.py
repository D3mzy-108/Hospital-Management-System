from django.shortcuts import render


# Create your views here.
def patient_dashboard(request):
    context = {}

    return render(request, 'dashboard/patient/home.html', context)


def doctor_dashboard(request):
    context = {}

    return render(request, 'dashboard/doctor/home.html', context)
