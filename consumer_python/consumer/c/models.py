# -*- coding: utf-8 -*-
from django.db import models

class Msg(models.Model):
    msg_text = models.CharField(max_length=200)
    msg_date = models.DateTimeField('date published')
