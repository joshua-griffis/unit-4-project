from pydoc import describe
from django.db import models
from pyparsing import Char
# Create your models here.


class Item(models.Model):
    name = models.TextField()
    description = models.TextField()
    image = models.TextField()
    price = models.IntegerField()
    cart = models.BooleanField()


def create_item(nam, desc, img, pri):
    return Item(name=nam, description=desc, image=img, price=pri, cart=False).save()


def add_to_cart(nam):
    item = Item.objects.get(name=nam)
    item.cart = True
    return item.save()
