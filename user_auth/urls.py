from django.urls import path

from user_auth.views import login, signup

urlpatterns = [
    path('', login, name="login"),
    path('sign-up/', signup, name="signup"),
]
