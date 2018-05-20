# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import Msg

# Create your views here.

def index(request):
    msg_list = Msg.objects.order_by('-msg_date')

    return render(request, 'c/index.html', {'msg_list': msg_list})
