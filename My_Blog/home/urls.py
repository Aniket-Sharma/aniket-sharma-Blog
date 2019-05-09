from django.contrib import admin
from django.urls import path, include
from .views import view_home_page 
urlpatterns = [
    path('', view_home_page.as_view(), name='homepage'),
]
