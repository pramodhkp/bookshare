from django.conf.urls.defaults import *
from bookshare.submitbook import views

urlpatterns = patterns('',
    (r'^submit/$', views.feed),
    (r'^feed/$', views.feed),
  
)
