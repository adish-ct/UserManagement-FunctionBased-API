from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import CustomUserCreationForm

# Create your views here.

def sample(request, *args, **kwargs):
    return HttpResponse(True, 200,)



