from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _

# Create your models here.
class List(models.Model):
    list = models.CharField(max_length=100, null=True, blank=True)

class Item(models.Model):
    #Event/ To-Do Item
    item = models.CharField(max_lenth=255, null=False, blank=False, verbose_name=_("To-Do item"))
    #Who created it
    user = models.ForeignKey(User, verbose_name=_("Event creator"), related_name="item_creator")
    #In what list was it created?
    list = models.ForeignKey(List, related_name="list_name_of_item", verbose_name=_("List name"))
    #In a given list, what is its order. This is computed every time we save
    order = models.PositiveIntegerField(blank=False, null=False)
    
    #Housekeeping stuff
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now = True)
    
    
    