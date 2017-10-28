from django.shortcuts import render

from django.http import  HttpResponse
from .models import Fill


def aindex(request):
    all_details=Fill.objects.all()
    return render(request,'aboutus/aindex.html',{'all_details':all_details})