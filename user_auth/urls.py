from django.urls import path

from user_auth.views import login, signup, edit_profile

urlpatterns = [
    path('', login, name="login"),
    path('sign-up/', signup, name="signup"),
    path('edit-profile/', edit_profile, name='edit')
]
