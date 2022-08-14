# pages/urls.py
# test_project/urls.py

from unicodedata import name
from django.urls import path, include

from django.contrib import admin

from .views import homePageView


urlpatterns = [    
    path('',homePageView, name = 'home'   )
]