from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def sample(request, *args, **kwargs):
    return HttpResponse(True, 200,)
