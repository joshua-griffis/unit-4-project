from app.views import *
from django.contrib import admin
from django.urls import path
from app import models

urlpatterns = [
    path('', root, name="root"),
    path('anime/', anime, name="anime"),
    path('cart/', cart, name="cart"),
    path('videogames/', videogames, name="videogames"),
    path('admin/', admin.site.urls),
]
