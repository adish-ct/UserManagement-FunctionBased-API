from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

from accounts.forms import CustomUserCreationForm

# Create your views here.

def register(request):
    """
    Register new users.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
        return redirect('register')
    form = CustomUserCreationForm()
    return render(request,'register.html', {'form': form})



def login_view(request):
    """
    Login users.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
        return redirect('login')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})









