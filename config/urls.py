from app.views import *
from django.contrib import admin
from django.urls import path
from app import models

urlpatterns = [
    path('', root, name="root"),
    path('admin/', admin.site.urls),
]
