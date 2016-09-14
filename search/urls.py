from django.conf.urls import patterns, url, include
from django.contrib import admin
from .views import search
	
urlpatterns = [
	url(r'.*', search)
	]