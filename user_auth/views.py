from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']

        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_staff:
            if user.is_active:
                auth.login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'invalid account')
                return render(request, 'user_auth/register.html')
        elif user is not None and not user.is_staff:
            if user.is_active:
                auth.login(request, user)
                return redirect('home')
            else:
                messages.warning(request, 'account is not active')
                return render(request, 'user_auth/register.html')
        else:
            messages.error(request, 'please enter valid details')
            return render(request, 'user_auth/register.html')
    context = {}
    return render(request, "user_auth/login.html",)

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff_type = 'none'
            instance.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
    }
    return render(request,"user_auth/register.html", context)