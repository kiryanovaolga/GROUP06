from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Room(models.Model):
    name = models.CharField(max_length=100)


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)


#-------------------------------------------------------------------------------


class ItemType(models.IntegerChoices):
    MOVIE = 1, 'Film'
    TV_SHOW = 2, 'Seriál'
    OTHER = 3, 'Ostatní'

class Genre(models.IntegerChoices):
    SCIFI = 1, 'Sci-fi'
    DRAMA = 2, 'Drama'
    COMERY = 3, 'Komedie'

class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    type = models.IntegerField(choices=ItemType)
    genre = models.IntegerField(choices=Genre)

class Review(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    rate = models.PositiveSmallIntegerField()

#-------------------------------------------------------------------------------
# OneToOneField = 1:1
# ForeignKey = 1:N
# ManyToManyField = M:N



class Product:
    name = models.CharField(max_length=100)
    image = models.ImageField()
    price = models.IntegerField()

class ProductItem:
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=100)

class Order:
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(ProductItem)



class Zamestnanec:
    name = models.CharField(max_length=100)
    boss = models.ForeignKey('self', on_delete=models.SET_NULL)
    # boss_id -> Zamestnanec.id


#-------------------------------------------------------------------------------
# jak customizovat User model
#-------------------------------------------------------------------------------

from django.contrib.auth.models import AbstractUser

class Services(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class User(AbstractUser):
    is_specialist = models.BooleanField(default=False)

    services = models.ManyToManyField(Services, blank=True)
