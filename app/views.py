from django.shortcuts import render
from app.forms import *

# Create your views here.


def root(request):
    print(request.POST)
    return render(request, 'root.html')
