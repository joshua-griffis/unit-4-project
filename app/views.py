from django.shortcuts import render
from app.forms import *

# Create your views here.


def root(request):
    form = HelloForm(request.GET)
    return render(request, 'root.html', {"form": form})
