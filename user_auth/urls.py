from django.urls import path

from user_auth.views import login

urlpatterns = [
    path('', login, name="login")
]