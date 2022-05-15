from importlib.resources import path
from xml.etree.ElementInclude import include
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import path
from. import views

app_name = 'blogsite'
urlpatterns = [
    path('', views.page_list.as_view(), name='home' ),
    path('<int:year>/<int:month>/<int:day>/<int:pk>/<slug:slug>',
    views.post_detail,
     name='post_detail'),
]