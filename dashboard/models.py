from django.db import models
from user_auth.models import User



# Create your models here.
class Appointment(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="doctor_appointments", null=True)
    reason = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointments")
    
    def __str__(self):
        return self.reason
