from django.conf.urls import url
from django.contrib import admin


app_name='aboutus'
from . import views
urlpatterns = [
    #/aboutus/
    url(r'^$', views.IndexView.as_view(),name='aindex'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
    url(r'fill/add/$',views.FillCreate.as_view(),name='fill-add'),

]
