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
         "price": "180,000",
         "cart": False},

        {"name": "Maxwell's Notebook",
         "desc": "This item is the notebook from the game Scribblenauts, the notebook that makes anything you write in it real.",
         "img": "images/maxwell's notebook.png",
         "price": "999,999,999,999",
         "cart": True},
    ]
    for item in content:
        create_item(item["name"], item["desc"],
                    item["img"], item["price"], item["cart"])
    return render(request, 'videogames.html', {"items": Item.objects.all()})


def anime(request):
    Item.objects.all().delete()
    content = [
        {"name": "The Renaissance Vase",
         "desc": "this item is the vase from the anime 'Oran Highschool Host Club'",
         "img": "images/vase.jpg",
         "price": "1,000",
         "cart": True},

        {"name": "Gomu Gomu no Mi",
         "desc": "This item is whats known as a devil's fruit the anime called One Piece",
         "img": "images/devil fruit.jpg",
         "price": "5,000,000,000",
         "cart": True},

        {"name": "Kurapika's Judgement Chain",
         "desc": "This item is one of the chains Kurapika uses in the anime Hunter X Hunter.",
         "img": "images/conjuration.gif",
         "price": "10,000,000",
         "cart": False},

        {"name": "Greed Island the video game",
         "desc": "This item is a very dangerous video game from the world of Hunter X Hunter.",
         "img": "images/greed island.jpg",
         "price": "8,000,000,000",
         "cart": False},

        {"name": "Ichigo Bankai",
         "desc": "This item is from the anime called BLEACH and the second form Zanpakuto.",
         "img": "images/Ichigo Bankai.jpg",
         "price": "100,000,000",
         "cart": False},

        {"name": "Sukuna Ryomen Finger",
         "desc": "This item is from the anime called Jujutsu Kaisen",
         "img": "images/finger.jpg",
         "price": "200,000,000,000",
         "cart": False},

        {"name": "Kisame's Blade, 'Samehada'",
         "desc": "this item is one of the most dangerous weapons of the Seven Ninja Swordsmen blades in Naruto",
         "img": "images/samehada.jpg",
         "price": "20,000,050",
         "cart": False},

        {"name": "The Deathnote Notebook",
         "desc": "This Notebook is a very dangerous notebook where whoever's name is written in it, they die shortly after.",
         "img": "images/deathnote.jpg",
         "price": "200,000,000,000",
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
