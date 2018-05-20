# -*- coding: utf-8 -*-
from django.urls import path
from c import views

urlpatterns = [
    path('', views.index, name='index'),
]
