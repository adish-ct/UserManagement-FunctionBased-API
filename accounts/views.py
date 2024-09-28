from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from accounts.forms import CustomUserCreationForm, CustomUserUpdateForm

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



@login_required(login_url='/login')
def update_profile(request):
    """
    Update user profile.
    """
    user = request.user
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
        return redirect('profile')
    form = CustomUserUpdateForm(instance=user)
    return render(request, 'profile.html', {'form': form})






