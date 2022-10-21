from pickle import GET
from django.shortcuts import render
from app.forms import *
from .models import *


# Create your views here.


def root(request):
    Item.objects.all().delete()
    content = [
        {"name": "The Renaissance Vase",
         "desc": "this item is from the anime 'Oran Highschool Host Club'",
         "img": "images/vase.jpg",
         "price": 1000,
         "cart": True},

        {"name": "Gomu Gomu no Mi",
         "desc": "This item is from the anime called One Piece",
         "img": "images/devil fruit.jpg",
         "price": 5000000000,
         "cart": True},
    ]
    for item in content:
        create_item(item["name"], item["desc"],
                    item["img"], item["price"], item["cart"])
    return render(request, 'root.html', {"items": Item.objects.all()})


def cart(request):
    liszt = []
    cart_items = Item.objects.filter(cart=True)
    for item in cart_items:
        liszt.append(item)
    return render(request, 'cart.html', {"cart": liszt})
