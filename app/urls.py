from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^search/', include('search.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)
