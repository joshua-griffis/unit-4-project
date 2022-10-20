from django.shortcuts import render
from app.forms import *
from dataclasses import dataclass
from .models import *

# Create your views here.


def root(request):

    return render(request, 'root.html')
