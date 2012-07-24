from django.conf.urls.defaults import patterns, url, include
from django.contrib import admin
from django.views.static import * 
from django.conf import settings

from app.views import home, dashboard, logout, error, form, form2
from submitbook.views import submit, feed
from userprofile.views import profile




admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^error/$', error, name='error'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^form/$', form, name='form'),
    url(r'^form2/$', form2, name='form2'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
    url(r'^messages/', include('postman.urls')),
    url('^activity/', include('actstream.urls')),
    url(r'^submit/$', submit, name='submit'),
    url(r'^feed/$', feed, name='feed'),
    url(r'^assets/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^profile/$', profile, name='profile'),

)
