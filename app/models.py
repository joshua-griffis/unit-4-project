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


def create_item(nam, desc, img, pri, cart):
    return Item(name=nam, description=desc, image=img, price=pri, cart=cart).save()
