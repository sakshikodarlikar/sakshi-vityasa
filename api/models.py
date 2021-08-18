# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Slot(models.Model):
    slot_id = models.IntegerField(primary_key=True)
    slot_1 = models.CharField(max_length=255,blank=True )
    slot_2 = models.CharField(max_length=255,blank=True )
    slot_booked = models.BooleanField(default=False)
    slot_date = models.DateField(blank=True, null=True)