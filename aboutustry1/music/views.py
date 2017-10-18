# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import  HttpResponse

def index(request):
    return HttpResponse("<h1>this is the music app homepage</h1>")

def detail(request,album_id):
    return HttpResponse("<h2>Details for album id:"+ str(album_id)+"</h2>")

