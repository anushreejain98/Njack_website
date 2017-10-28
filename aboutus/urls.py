from django.conf.urls import url
from django.contrib import admin
app_name='aboutus'
from . import views
urlpatterns = [
    #/aboutus/
    url(r'^$', views.aindex,name='aindex'),


]
