from pickle import GET
from django.shortcuts import render
from app.forms import *
from .models import *


# Create your views here.

def root(request):
    return render(request, 'root.html')


def videogames(request):
    Item.objects.all().delete()
    content = [
        {"name": "Diamond Pickaxe",
         "desc": "This item is pretty self explanatory, its a pickaxe made of diamonds from the video game Minecraft.",
         "img": "images/diamond pickaxe.gif",
         "price": 180000,
         "cart": False},
    ]
    for item in content:
        create_item(item["name"], item["desc"],
                    item["img"], item["price"], item["cart"])
    return render(request, 'videogames.html', {"items": Item.objects.all()})


def anime(request):
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

        {"name": "Kurapika's Judgement Chain",
         "desc": "This item is one of the chains Kurapika uses in the anime Hunter X Hunter.",
         "img": "images/conjuration.gif",
         "price": 10000000,
         "cart": False},

        {"name": "Greed Island the video game",
         "desc": "This item is a very dangerous video game from the world of Hunter X Hunter.",
         "img": "images/greed island.jpg",
         "price": 8000000000,
         "cart": False},
         
        {"name": "Ichigo Bankai",
        "desc": "This item is from the anime called BLEACH and the second form Zanpakuto.",
        "img": "images/Ichigo Bankai.jpg",
        "price": "100000000",
        "cart": False},
    ]
    for item in content:
        create_item(item["name"], item["desc"],
                    item["img"], item["price"], item["cart"])
    return render(request, 'anime.html', {"items": Item.objects.all()})


def cart(request):
    liszt = []
    cart_items = Item.objects.filter(cart=True)
    for item in cart_items:
        liszt.append(item)
    return render(request, 'cart.html', {"cart": liszt})
