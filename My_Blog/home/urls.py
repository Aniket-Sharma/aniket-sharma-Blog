from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', view_home_page.as_view(), name='homepage'),
    path('about/', view_about_page.as_view(), name='about'),
]
