from django.conf.urls import url

from . import views


urlpatterns = [

    url(r'^zip\/\d{5}', views.zipsearch, name='zipsearch'),



    url(r'^/', views.index, name='index'),


]