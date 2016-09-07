from django.conf.urls import patterns, url, include
import views

urlpatterns = patterns('',
url(r'^$', views.index, name='index'),
url(r'^searchcar/$', views.searchResults, name='searchResults'),
)
