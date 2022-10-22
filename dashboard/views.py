from django.shortcuts import render, redirect
from dashboard.models import Appointment
from user_auth.models import User


# Create your views here.
def patient_dashboard(request, username):
    appointments = request.user.appointments.all().order_by('-date')
    doctors = User.objects.filter(staff_type="doctor")
    
    context = {
        'appointments': appointments,
        'doctors': doctors,
    }

    return render(request, 'dashboard/patient/home.html', context)


def create_appointment(request):
    if request.method == "POST":
        doctor = request.POST['doctor']
        reason = request.POST['reason']
        date = request.POST['date']
        time = request.POST['time']
        client = request.user
        
        Appointment(doctor=User.objects.get(pk=doctor), reason=reason, date=date, time=time, client=client).save()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('patient_dashboard', request.user.username)


def reschedule_appointment(request, pk):
    if request.method == "POST":
        date = request.POST['edit_date']
        time = request.POST['edit_time']
        
        appointment = Appointment.objects.get(pk=pk)
        appointment.date = date
        appointment.time = time
        appointment.save()
        
    return redirect('patient_dashboard', request.user.username)


def doctor_dashboard(request, username):
    context = {}

    return render(request, 'dashboard/doctor/home.html', context)
