from django.shortcuts import render
from app.forms import *
from .models import *
from django.views.generic import CreateView

# Create your views here.


def root(request):
    Item.objects.all().delete()
    content = [
        {"name": "The Renaissance Vase",
         "desc": "this item is from the anime 'Oran Highschool Host Club'",
         "img": "images/vase.jpg",
         "price": 1000},

        {"name": "item",
         "desc": "this item is an example item",
         "img": "images/conjuration.gif",
         "price": 10},
    ]
    for item in content:
        create_item(item["name"], item["desc"],
                    item["img"], item["price"])
    return render(request, 'root.html', {"items": Item.objects.all()})


def cart(request):
    liszt = []
    cart_items = Item.objects.filter(cart=True)
    for item in cart_items:
        liszt.append(item)
    return render(request, 'cart.html', {"cart": liszt})
